#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place asyncer docs_src tests --exclude=__init__.py
black asyncer tests docs_src
isort asyncer tests docs_src
