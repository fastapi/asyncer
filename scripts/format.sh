#!/bin/sh -e
set -x

ruff check asyncer tests docs_src --fix
ruff format asyncer tests docs_src
