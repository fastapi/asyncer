# Release Notes

## Latest Changes

### Internal

* 👷 Update `labeler.yml`. PR [#238](https://github.com/fastapi/asyncer/pull/238) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update worfkow deploy-docs-notify URL. PR [#235](https://github.com/fastapi/asyncer/pull/235) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade Cloudflare GitHub Action. PR [#234](https://github.com/fastapi/asyncer/pull/234) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump mkdocs-macros-plugin from 1.0.5 to 1.2.0. PR [#220](https://github.com/fastapi/asyncer/pull/220) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.6.4 to 0.6.5. PR [#221](https://github.com/fastapi/asyncer/pull/221) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest requirement from <8.0.0,>=7.0.1 to >=7.0.1,<9.0.0. PR [#207](https://github.com/fastapi/asyncer/pull/207) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.6.2 to 0.6.4. PR [#217](https://github.com/fastapi/asyncer/pull/217) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.5.0 to 0.5.1. PR [#219](https://github.com/fastapi/asyncer/pull/219) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.10.1. PR [#216](https://github.com/fastapi/asyncer/pull/216) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.5.18 to 9.5.34. PR [#212](https://github.com/fastapi/asyncer/pull/212) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#209](https://github.com/fastapi/asyncer/pull/209) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump typer from 0.12.3 to 0.12.5. PR [#208](https://github.com/fastapi/asyncer/pull/208) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mypy from 1.11.1 to 1.11.2. PR [#206](https://github.com/fastapi/asyncer/pull/206) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update `issue-manager.yml`. PR [#218](https://github.com/fastapi/asyncer/pull/218) by [@tiangolo](https://github.com/tiangolo).
* 💚 Set `include-hidden-files` to `True` when using the `upload-artifact` GH action. PR [#215](https://github.com/fastapi/asyncer/pull/215) by [@svlandeg](https://github.com/svlandeg).
* 👷 Update `latest-changes` GitHub Action. PR [#203](https://github.com/fastapi/asyncer/pull/203) by [@tiangolo](https://github.com/tiangolo).

## 0.0.8

### Refactors

* ♻️ Deprecate `asyncify(cancellable=True)` in favor of `asyncify(abandon_on_cancel=True)`, following AnyIO 4.1.0. PR [#202](https://github.com/fastapi/asyncer/pull/202) by [@tiangolo](https://github.com/tiangolo).
* ♻️ Import `anyio.from_thread` and `anyio.to_thread` explicitly. PR [#201](https://github.com/fastapi/asyncer/pull/201) by [@tiangolo](https://github.com/tiangolo).
* ♻️ Update `asyncify` to wrap the function with `functools.wraps` like the other functions. PR [#84](https://github.com/fastapi/asyncer/pull/84) by [@Gowee](https://github.com/Gowee).

### Docs

* 📝 Add docs references to FastAPI's docs on virtual environments and new contributing guide. PR [#200](https://github.com/fastapi/asyncer/pull/200) by [@tiangolo](https://github.com/tiangolo).
* 📝 Add docs about repo management and team. PR [#184](https://github.com/tiangolo/asyncer/pull/184) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆ Bump actions/cache from 3 to 4. PR [#114](https://github.com/fastapi/asyncer/pull/114) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.8.11 to 1.9.0. PR [#164](https://github.com/fastapi/asyncer/pull/164) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 10.1.0 to 10.4.0. PR [#167](https://github.com/fastapi/asyncer/pull/167) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.2.0 to 0.6.2. PR [#199](https://github.com/fastapi/asyncer/pull/199) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#157](https://github.com/fastapi/asyncer/pull/157) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mypy from 1.4.1 to 1.11.1. PR [#171](https://github.com/fastapi/asyncer/pull/171) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔥 Remove unused scripts. PR [#197](https://github.com/fastapi/asyncer/pull/197) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update converage configs. PR [#196](https://github.com/fastapi/asyncer/pull/196) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Add URLs to `pyproject.toml`, show up in PyPI. PR [#195](https://github.com/fastapi/asyncer/pull/195) by [@tiangolo](https://github.com/tiangolo).
* 👷 Do not sync labels as it overrides manually added labels. PR [#194](https://github.com/fastapi/asyncer/pull/194) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update GitHub Action labeler to put only one label. PR [#192](https://github.com/fastapi/asyncer/pull/192) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update GitHub Action labeler permissions and dependencies. PR [#191](https://github.com/fastapi/asyncer/pull/191) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action label-checker. PR [#190](https://github.com/fastapi/asyncer/pull/190) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action labeler. PR [#189](https://github.com/fastapi/asyncer/pull/189) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update GitHub Action add-to-project. PR [#188](https://github.com/fastapi/asyncer/pull/188) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add GitHub Action add-to-project. PR [#187](https://github.com/fastapi/asyncer/pull/187) by [@tiangolo](https://github.com/tiangolo).
* 📝 Change links from github.com/tiangolo/asyncer to github.com/fastapi/asyncer. PR [#186](https://github.com/fastapi/asyncer/pull/186) by [@tiangolo](https://github.com/tiangolo).
* 🔨 Update docs.py script to enable dirty reload conditionally. PR [#185](https://github.com/tiangolo/asyncer/pull/185) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update MkDocs previews. PR [#183](https://github.com/tiangolo/asyncer/pull/183) by [@tiangolo](https://github.com/tiangolo).
* 💄 Update Termynal line-height. PR [#181](https://github.com/tiangolo/asyncer/pull/181) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade build docs configs. PR [#180](https://github.com/tiangolo/asyncer/pull/180) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add alls-green for test-redistribute. PR [#178](https://github.com/tiangolo/asyncer/pull/178) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update docs-previews to handle no docs changes. PR [#179](https://github.com/tiangolo/asyncer/pull/179) by [@tiangolo](https://github.com/tiangolo).
* 👷 Show docs deployment status and preview URLs in comment. PR [#177](https://github.com/tiangolo/asyncer/pull/177) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Enable auto dark mode. PR [#175](https://github.com/tiangolo/asyncer/pull/175) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager. PR [#174](https://github.com/tiangolo/asyncer/pull/174) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update issue-manager.yml GitHub Action permissions. PR [#173](https://github.com/tiangolo/asyncer/pull/173) by [@tiangolo](https://github.com/tiangolo).
* 👷 Refactor GitHub Action to comment docs deployment URLs and update token, preparing for GitHub org. PR [#172](https://github.com/tiangolo/asyncer/pull/172) by [@tiangolo](https://github.com/tiangolo).
* 🔨 Update docs Termynal scripts to not include line nums for local dev. PR [#169](https://github.com/tiangolo/asyncer/pull/169) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump mkdocs-material from 9.4.7 to 9.5.24. PR [#162](https://github.com/tiangolo/asyncer/pull/162) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update GitHub Actions to download and upload artifacts. PR [#159](https://github.com/tiangolo/asyncer/pull/159) by [@tiangolo](https://github.com/tiangolo).
* 👷 Tweak CI for test-redistribute, add needed env vars for slim. PR [#158](https://github.com/tiangolo/asyncer/pull/158) by [@tiangolo](https://github.com/tiangolo).

## 0.0.7

### Internal

* 🔧 Add configs for asyncer-slim. PR [#152](https://github.com/tiangolo/asyncer/pull/152) by [@tiangolo](https://github.com/tiangolo).

In the future Asyncer can include the standard default recommended packages, and `asyncer-slim` can come without those recommended standard packages and with a group of optional dependencies `asyncer-slim[standard]`, equivalent to `asyncer`, for those that want to opt out of those packages.

## 0.0.6

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#122](https://github.com/tiangolo/asyncer/pull/122) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump dorny/paths-filter from 2 to 3. PR [#118](https://github.com/tiangolo/asyncer/pull/118) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.28.0 to 3.1.4. PR [#137](https://github.com/tiangolo/asyncer/pull/137) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔨 Update internal scripts and remove unused ones. PR [#149](https://github.com/tiangolo/asyncer/pull/149) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Migrate from Poetry to PDM for handling the internal dependencies and build. PR [#148](https://github.com/tiangolo/asyncer/pull/148) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add cron to run test once a week on monday. PR [#140](https://github.com/tiangolo/asyncer/pull/140) by [@estebanx64](https://github.com/estebanx64).
* ⬆️ Upgrade Ruff version and configs. PR [#139](https://github.com/tiangolo/asyncer/pull/139) by [@tiangolo](https://github.com/tiangolo).

## 0.0.5

### Fixes

* 🐛  Fix `syncify` with `raise_sync_error=False` on AnyIO 4.x.x, do not start new event loops unnecessarily. PR [#130](https://github.com/tiangolo/asyncer/pull/130) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 👷 Update Publish CI Python version to 3.11. PR [#120](https://github.com/tiangolo/asyncer/pull/120) by [@tiangolo](https://github.com/tiangolo).

## 0.0.4

### Docs

* 📝 Update docstring for `syncify()`, fix name of parameter `raise_sync_error` (remove unused parameter name `check_called_from_async`). PR [#113](https://github.com/tiangolo/asyncer/pull/113) by [@giladsheffer](https://github.com/giladsheffer).

### Internal

* 🔧 Add Ruff config. PR [#112](https://github.com/tiangolo/asyncer/pull/112) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Adopt Ruff for formatting and linting and upgrade internal tools. PR [#111](https://github.com/tiangolo/asyncer/pull/111) by [@tiangolo](https://github.com/tiangolo).

## 0.0.3

### Features

* ✨ Export (import and re-export) `TaskGroup` from `asyncer`. PR [#87](https://github.com/tiangolo/asyncer/pull/87) by [@MarkParker5](https://github.com/MarkParker5).
* ✨ Add support for AnyIO 4.x, drop support for Python 3.7. PR [#90](https://github.com/tiangolo/asyncer/pull/90) by [@khiemdoan](https://github.com/khiemdoan).

### Fixes

* 🐛 Add missing dependency `typing_extensions` for Python < 3.10. PR [#89](https://github.com/tiangolo/asyncer/pull/89) by [@ZhymabekRoman](https://github.com/ZhymabekRoman).

### Refactors

* ✏️ Tweak docstrings format. PR [#50](https://github.com/tiangolo/asyncer/pull/50) by [@realFranco](https://github.com/realFranco).

### Docs

* 👷 Upgrade CI for docs. PR [#78](https://github.com/tiangolo/asyncer/pull/78) by [@tiangolo](https://github.com/tiangolo).
* 🛠️ Tweak internal CI actions, add `--no-cache-dir` at `Dockfile` files. PR [#52](https://github.com/tiangolo/asyncer/pull/52) by [@realFranco](https://github.com/realFranco).
* 📝 Update help Asyncer docs. PR [#65](https://github.com/tiangolo/asyncer/pull/65) by [@tiangolo](https://github.com/tiangolo).
* 🍱 Update logo vector asset, do not depend on system fonts. PR [#60](https://github.com/tiangolo/asyncer/pull/60) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 🔧 Update classifiers for Python 3.11 and Python 3.12. PR [#110](https://github.com/tiangolo/asyncer/pull/110) by [@tiangolo](https://github.com/tiangolo).
* 👷 Enable tests for Python 3.12 in CI. PR [#108](https://github.com/tiangolo/asyncer/pull/108) by [@khiemdoan](https://github.com/khiemdoan).
* ⬆ Bump actions/setup-python from 4 to 5. PR [#102](https://github.com/tiangolo/asyncer/pull/102) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.4.0 to 0.4.1. PR [#109](https://github.com/tiangolo/asyncer/pull/109) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update build docs cache key. PR [#103](https://github.com/tiangolo/asyncer/pull/103) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade latest-changes. PR [#101](https://github.com/tiangolo/asyncer/pull/101) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update latest changes GitHub Action to use the latest release. PR [#100](https://github.com/tiangolo/asyncer/pull/100) by [@tiangolo](https://github.com/tiangolo).
* 📝 Fix duplicated docs and latest-changes GitHub Action version. PR [#99](https://github.com/tiangolo/asyncer/pull/99) by [@tiangolo](https://github.com/tiangolo).
* 👷 Upgrade latest-changes. PR [#97](https://github.com/tiangolo/asyncer/pull/97) by [@tiangolo](https://github.com/tiangolo).
* 📝 Tweak release notes with latest changes. PR [#98](https://github.com/tiangolo/asyncer/pull/98) by [@tiangolo](https://github.com/tiangolo).
* 🔨 Update dev scripts. PR [#95](https://github.com/tiangolo/asyncer/pull/95) by [@tiangolo](https://github.com/tiangolo).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#83](https://github.com/tiangolo/asyncer/pull/83) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/checkout from 3 to 4. PR [#85](https://github.com/tiangolo/asyncer/pull/85) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.27.0 to 2.28.0. PR [#88](https://github.com/tiangolo/asyncer/pull/88) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Install MkDocs Material Insiders only when secrets are available, for Dependabot. PR [#94](https://github.com/tiangolo/asyncer/pull/94) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Add `CITATION.cff` file for academic citations. PR [#92](https://github.com/tiangolo/asyncer/pull/92) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update Debug mode with Tmate for CI. PR [#82](https://github.com/tiangolo/asyncer/pull/82) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update docs deploy to Cloudflare pages. PR [#81](https://github.com/tiangolo/asyncer/pull/81) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update docs CI, main branch is main, not master. PR [#80](https://github.com/tiangolo/asyncer/pull/80) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update dependencies now that 3.6 is deprecated. PR [#79](https://github.com/tiangolo/asyncer/pull/79) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump nwtgck/actions-netlify from 1.2.4 to 2.0.0. PR [#58](https://github.com/tiangolo/asyncer/pull/58) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.2 to 2.27.0. PR [#74](https://github.com/tiangolo/asyncer/pull/74) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#57](https://github.com/tiangolo/asyncer/pull/57) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Update token for latest changes. PR [#70](https://github.com/tiangolo/asyncer/pull/70) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade analytics. PR [#67](https://github.com/tiangolo/asyncer/pull/67) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update new issue chooser to point to Discussions. PR [#64](https://github.com/tiangolo/asyncer/pull/64) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Add question template for GitHub Discussions and update issues template. PR [#63](https://github.com/tiangolo/asyncer/pull/63) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Upgrade isort and pre-commit config. PR [#62](https://github.com/tiangolo/asyncer/pull/62) by [@tiangolo](https://github.com/tiangolo).
* 👷 Refactor CI artifact upload/download for docs previews. PR [#59](https://github.com/tiangolo/asyncer/pull/59) by [@tiangolo](https://github.com/tiangolo).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#56](https://github.com/tiangolo/asyncer/pull/56) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/cache from 2 to 3. PR [#55](https://github.com/tiangolo/asyncer/pull/55) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.1 to 2.24.2. PR [#54](https://github.com/tiangolo/asyncer/pull/54) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.9.0 to 2.24.1. PR [#53](https://github.com/tiangolo/asyncer/pull/53) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.0.2

### Features

* ✨ Add compatibility with the next (unreleased) version of AnyIO (4.x.x), with `get_asynclib` utility. PR [#48](https://github.com/tiangolo/asyncer/pull/48) by [@tiangolo](https://github.com/tiangolo).

### Docs

* ✏ Fix link to FastAPI and Friends newsletter. PR [#13](https://github.com/tiangolo/asyncer/pull/13) by [@JonasKs](https://github.com/JonasKs).
* ✏ Fix typo in `docs/tutorial/first-steps.md`, from `asyncio` to `anyio`. PR [#11](https://github.com/tiangolo/asyncer/pull/11) by [@windson](https://github.com/windson).
* ✏️ Fix broken link in README and index. PR [#9](https://github.com/tiangolo/asyncer/pull/9) by [@vrslev](https://github.com/vrslev).
* ✏ Fix typo in `syncify-no-raise.md`. PR [#6](https://github.com/tiangolo/asyncer/pull/6) by [@Kludex](https://github.com/Kludex).

### Internal

* 🔧 Update mypy config, use `strict = true` instead of manual configs. PR [#38](https://github.com/tiangolo/asyncer/pull/38) by [@michaeloliverx](https://github.com/michaeloliverx).
* ➕ Add extra dev dependencies for MkDocs Material. PR [#49](https://github.com/tiangolo/asyncer/pull/49) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Update mypy requirement from ^0.930 to ^0.971. PR [#34](https://github.com/tiangolo/asyncer/pull/34) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update black requirement from ^21.5-beta.1 to ^22.10.0. PR [#41](https://github.com/tiangolo/asyncer/pull/41) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#31](https://github.com/tiangolo/asyncer/pull/31) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump nwtgck/actions-netlify from 1.1.5 to 1.2.4. PR [#47](https://github.com/tiangolo/asyncer/pull/47) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 2 to 3. PR [#46](https://github.com/tiangolo/asyncer/pull/46) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 2 to 4. PR [#45](https://github.com/tiangolo/asyncer/pull/45) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 2 to 3. PR [#44](https://github.com/tiangolo/asyncer/pull/44) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pytest requirement from ^6.2.4 to ^7.0.1. PR [#18](https://github.com/tiangolo/asyncer/pull/18) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update flake8 requirement from ^4.0.1 to ^5.0.4. PR [#37](https://github.com/tiangolo/asyncer/pull/37) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Update Dependabot config. PR [#43](https://github.com/tiangolo/asyncer/pull/43) by [@tiangolo](https://github.com/tiangolo).
* 👷 Move from Codecov to Smokeshow. PR [#42](https://github.com/tiangolo/asyncer/pull/42) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Add pre-commit and format. PR [#28](https://github.com/tiangolo/asyncer/pull/28) by [@tiangolo](https://github.com/tiangolo).
* 💚 Fix installing Material for MkDocs Insiders in CI. PR [#27](https://github.com/tiangolo/asyncer/pull/27) by [@tiangolo](https://github.com/tiangolo).
* 👷 Disable installing MkDocs Insiders in forks. PR [#26](https://github.com/tiangolo/asyncer/pull/26) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Upgrade Codecov GitHub Action. PR [#23](https://github.com/tiangolo/asyncer/pull/23) by [@tiangolo](https://github.com/tiangolo).
* 💚 Only run CI on push when on master, to avoid duplicate runs for PRs. PR [#17](https://github.com/tiangolo/asyncer/pull/17) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Update flake8 requirement from ^3.9.2 to ^4.0.1. PR [#3](https://github.com/tiangolo/asyncer/pull/3) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update coverage requirement from ^5.5 to ^6.2. PR [#1](https://github.com/tiangolo/asyncer/pull/1) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Upgrade MkDocs Material and update configs. PR [#10](https://github.com/tiangolo/asyncer/pull/10) by [@tiangolo](https://github.com/tiangolo).

## 0.0.1

* First release. 🎉

### Docs

* ✏ Fix typo in index and README. PR [#4](https://github.com/tiangolo/asyncer/pull/4) by [@sanders41](https://github.com/sanders41).
