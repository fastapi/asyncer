#!/usr/bin/env bash

set -e
set -x

mypy asyncer
ty check asyncer
ruff check asyncer tests docs_src
ruff format asyncer tests docs_src --check
