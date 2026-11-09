#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

CONF="book/conf.py"
EXTENSION_PATH="sys.path.insert(0, os.path.join(os.path.dirname(__file__), '_ext'))"
TOC_PATH="external_toc_path = '_toc_with_local_paths.yml'"
AUTHORS_SETTING="git_show_all_authors = False"
LINKCHECK_SETTING="html_linkcheck_enabled = False"

jupyter-book config sphinx book/

sed -i "/# re-generate this one/a\\
import os\\
import sys\\
\\
$EXTENSION_PATH" "$CONF"
sed -i 's/git_show_all_authors = True/git_show_all_authors = False/' "$CONF"
sed -i "s/external_toc_path = '_toc.yml'/$TOC_PATH/" "$CONF"
printf '\n%s\n' "$LINKCHECK_SETTING" >> "$CONF"

grep -Fq "$EXTENSION_PATH" "$CONF"
grep -Fq "$TOC_PATH" "$CONF"
grep -Fq "$AUTHORS_SETTING" "$CONF"
grep -Fqx "$LINKCHECK_SETTING" "$CONF"

teachbooks build book/ --process-only
