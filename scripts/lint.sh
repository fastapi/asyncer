#!/usr/bin/env bash

set -e
set -x

mypy asyncer
ruff check asyncer tests docs_src
black asyncer tests docs_src --check
