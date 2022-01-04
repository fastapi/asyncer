#!/usr/bin/env bash

set -e
set -x

mypy asyncer
flake8 asyncer tests docs_src
black asyncer tests docs_src --check
isort asyncer tests docs_src scripts --check-only
