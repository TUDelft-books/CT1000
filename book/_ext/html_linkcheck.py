"""Check external links in pages written by the HTML builder."""

import json
import re
from urllib.parse import urlsplit

from docutils import nodes
from requests.exceptions import RequestException
from sphinx.builders.linkcheck import (
    Hyperlink,
    HyperlinkAvailabilityChecker,
    _get_request_headers,
)
from sphinx.util import logging
from sphinx.util import requests
from sphinx.util.nodes import get_node_line

logger = logging.getLogger(__name__)

TEACHBOOKS_REDIRECT = re.compile(
    r"let\s+currentUrl\s*=\s*window\.location\.href\s*;"
    r"[\s\S]*?let\s+urlParts\s*=\s*currentUrl\.split\('/'\)\s*;"
    r"[\s\S]*?let\s+bname\s*=\s*urlParts\[4\]\s*;"
    r"[\s\S]*?let\s+branches\s*=\s*(\[[^\]]*\])\s*;"
    r"[\s\S]*?if\s*\(\s*!branches\.includes\(bname\)\s*\)\s*\{"
    r"[\s\S]*?urlParts\.splice\(4,\s*0,\s*'([A-Za-z0-9._-]+)'\)\s*;"
    r"[\s\S]*?let\s+newUrl\s*=\s*urlParts\.join\('/'\)\s*;"
    r"[\s\S]*?window\.location\.href\s*=\s*newUrl\s*;"
)


def teachbooks_redirect(uri, html):
    for script in re.findall(r"<script\b[^>]*>([\s\S]*?)</script\s*>", html, re.I):
        match = TEACHBOOKS_REDIRECT.search(script)
        if not match:
            continue
        try:
            branches = json.loads(match.group(1))
        except ValueError:
            continue
        if not isinstance(branches, list) or not all(
            isinstance(branch, str) for branch in branches
        ):
            continue
        parts = uri.split("/")
        if len(parts) < 4 or (len(parts) > 4 and parts[4] in branches):
            return None
        parts.insert(4, match.group(2))
        return "/".join(parts)
    return None


def find_teachbooks_redirect(app, uri):
    headers = _get_request_headers(uri, app.config.linkcheck_request_headers)
    auth = next(
        (value for pattern, value in app.config.linkcheck_auth if re.match(pattern, uri)),
        None,
    )
    with requests.get(
        uri,
        headers=headers,
        auth=auth,
        timeout=app.config.linkcheck_timeout,
        stream=True,
        _user_agent=app.config.user_agent,
        _tls_info=(app.config.tls_verify, app.config.tls_cacerts),
    ) as response:
        if response.status_code != 404:
            return None
        content = bytearray()
        for chunk in response.iter_content(chunk_size=8192):
            content.extend(chunk)
            if len(content) > 262144:
                return None
        url = response.url
        original_fragment = urlsplit(uri).fragment
        if original_fragment and not urlsplit(url).fragment:
            url += "#" + original_fragment
        return teachbooks_redirect(url, content.decode(response.encoding or "utf-8", errors="replace"))


def report_broken(app, result, detail=None):
    logger.info(
        "BROKEN LINK: %s:%s: %s (%s)",
        app.env.doc2path(result.docname),
        result.lineno,
        result.uri,
        detail or result.message,
    )


def collect_links(app, doctree, docname):
    if not app.config.html_linkcheck_enabled or app.builder.format != "html":
        return

    for node in doctree.findall():
        uri = None
        if isinstance(node, nodes.reference):
            uri = node.get("refuri")
        elif isinstance(node, nodes.image):
            uri = node.get("candidates", {}).get("?")
        elif isinstance(node, nodes.raw):
            uri = node.get("source")

        if not uri or not uri.startswith(("http://", "https://")):
            continue

        uri = app.emit_firstresult("linkcheck-process-uri", uri) or uri
        try:
            line = get_node_line(node)
        except ValueError:
            line = -1
        app.html_linkcheck_links.setdefault(
            uri, Hyperlink(uri, docname, app.env.doc2path(docname), line)
        )


def check_links(app, exception):
    if (
        exception is not None
        or not app.config.html_linkcheck_enabled
        or app.builder.format != "html"
    ):
        return

    checker = HyperlinkAvailabilityChecker(app.config)
    redirects = {}
    for result in checker.check(app.html_linkcheck_links):
        if result.status == "broken":
            target = None
            if result.message.startswith("404 Client Error:"):
                try:
                    target = find_teachbooks_redirect(app, result.uri)
                except RequestException as error:
                    logger.info(
                        "LINK CHECK INCOMPLETE: %s:%s: %s "
                        "(could not inspect 404 response: %s)",
                        app.env.doc2path(result.docname),
                        result.lineno,
                        result.uri,
                        error,
                    )
                    continue
            if target:
                redirects.setdefault(target, []).append(result)
            else:
                report_broken(app, result)
        elif result.status in ("timeout", "unknown", ""):
            logger.info(
                "LINK CHECK INCOMPLETE: %s:%s: %s (%s)",
                app.env.doc2path(result.docname),
                result.lineno,
                result.uri,
                result.message or result.status or "unknown status",
            )

    if redirects:
        hyperlinks = {
            target: Hyperlink(
                target, results[0].docname, app.env.doc2path(results[0].docname),
                results[0].lineno,
            )
            for target, results in redirects.items()
        }
        for result in HyperlinkAvailabilityChecker(app.config).check(hyperlinks):
            for original in redirects[result.uri]:
                if result.status == "broken":
                    report_broken(
                        app, original,
                        f"TeachBooks redirect to {result.uri}: {result.message}",
                    )
                elif result.status not in ("working", "redirected"):
                    logger.info(
                        "LINK CHECK INCOMPLETE: %s:%s: %s "
                        "(TeachBooks redirect to %s: %s)",
                        app.env.doc2path(original.docname),
                        original.lineno,
                        original.uri,
                        result.uri,
                        result.message or result.status or "unknown status",
                    )


def setup(app):
    app.add_config_value("html_linkcheck_enabled", True, "html", types=[bool])
    app.html_linkcheck_links = {}
    app.connect("doctree-resolved", collect_links)
    app.connect("build-finished", check_links)
    return {"parallel_read_safe": True, "parallel_write_safe": False}
