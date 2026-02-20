# Release Notes

## Latest Changes

## 0.0.15

### Breaking Changes

* ➖ Drop support for Python 3.9. PR [#476](https://github.com/fastapi/asyncer/pull/476) by [@tiangolo](https://github.com/tiangolo).

### Internal

* 🔨 Update script to generate source examples, migrate from Python 3.9 to Python 3.10. PR [#478](https://github.com/fastapi/asyncer/pull/478) by [@tiangolo](https://github.com/tiangolo).
* 👷 Remove min-max testing of AnyIO, covered by uv resolution. PR [#477](https://github.com/fastapi/asyncer/pull/477) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump ruff from 0.15.1 to 0.15.2. PR [#475](https://github.com/fastapi/asyncer/pull/475) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.7.1 to 9.7.2. PR [#474](https://github.com/fastapi/asyncer/pull/474) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.23.1 to 0.23.2. PR [#473](https://github.com/fastapi/asyncer/pull/473) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.0.14

### Internal

* 👷 Run tests with lower bound uv sync, upgrade `pytest` minimum dependency pin. PR [#464](https://github.com/fastapi/asyncer/pull/464) by [@YuriiMotov](https://github.com/YuriiMotov).
* ⬆ Bump prek from 0.3.2 to 0.3.3. PR [#471](https://github.com/fastapi/asyncer/pull/471) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.23.0 to 0.23.1. PR [#470](https://github.com/fastapi/asyncer/pull/470) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.15.0 to 0.15.1. PR [#469](https://github.com/fastapi/asyncer/pull/469) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.21.1 to 0.23.0. PR [#468](https://github.com/fastapi/asyncer/pull/468) by [@dependabot[bot]](https://github.com/apps/dependabot).

## 0.0.13

### Docs

* 📝 Update management-tasks.md to be in line with management-tasks.md in FastAPI repo. PR [#462](https://github.com/fastapi/asyncer/pull/462) by [@YuriiMotov](https://github.com/YuriiMotov).
* 📝 Add contribution instructions about LLM generated code and comments and automated tools for PRs. PR [#449](https://github.com/fastapi/asyncer/pull/449) by [@alejsdev](https://github.com/alejsdev).
* 🐛 Fix copy button in `custom.js`. PR [#448](https://github.com/fastapi/asyncer/pull/448) by [@alejsdev](https://github.com/alejsdev).

### Internal

* 🔨 Tweak PDM hook and build process for `asyncer-slim`. PR [#467](https://github.com/fastapi/asyncer/pull/467) by [@tiangolo](https://github.com/tiangolo).
* 👷 Update build setup for `asyncer-slim`, deprecate it, and make it only depend on `asyncer`. PR [#466](https://github.com/fastapi/asyncer/pull/466) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump prek from 0.3.1 to 0.3.2. PR [#463](https://github.com/fastapi/asyncer/pull/463) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.14 to 0.15.0. PR [#461](https://github.com/fastapi/asyncer/pull/461) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Add generate-readme to pre-commit. PR [#460](https://github.com/fastapi/asyncer/pull/460) by [@tiangolo](https://github.com/tiangolo).
* 👷 Run mypy by pre-commit. PR [#459](https://github.com/fastapi/asyncer/pull/459) by [@YuriiMotov](https://github.com/YuriiMotov).
* ⬆ Bump ruff from 0.14.13 to 0.14.14. PR [#457](https://github.com/fastapi/asyncer/pull/457) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump prek from 0.3.0 to 0.3.1. PR [#458](https://github.com/fastapi/asyncer/pull/458) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump prek from 0.2.30 to 0.3.0. PR [#456](https://github.com/fastapi/asyncer/pull/456) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump prek from 0.2.25 to 0.2.30. PR [#454](https://github.com/fastapi/asyncer/pull/454) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump anyio from 4.12.0 to 4.12.1. PR [#451](https://github.com/fastapi/asyncer/pull/451) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.21.0 to 0.21.1. PR [#452](https://github.com/fastapi/asyncer/pull/452) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mypy from 1.14.1 to 1.19.1. PR [#453](https://github.com/fastapi/asyncer/pull/453) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.10 to 0.14.13. PR [#450](https://github.com/fastapi/asyncer/pull/450) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Ensure that an edit to `uv.lock` gets the `internal` label. PR [#455](https://github.com/fastapi/asyncer/pull/455) by [@svlandeg](https://github.com/svlandeg).
* 👷 Update Smokeshow, use uv. PR [#447](https://github.com/fastapi/asyncer/pull/447) by [@tiangolo](https://github.com/tiangolo).
* ⬆️ Migrate to uv. PR [#440](https://github.com/fastapi/asyncer/pull/440) by [@DoctorJohn](https://github.com/DoctorJohn).
* ✅ Expand test matrix to include Windows and MacOS. PR [#392](https://github.com/fastapi/asyncer/pull/392) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump typer from 0.20.0 to 0.21.0. PR [#444](https://github.com/fastapi/asyncer/pull/444) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/cache from 4 to 5. PR [#428](https://github.com/fastapi/asyncer/pull/428) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump markdown-include-variants from 0.0.5 to 0.0.8. PR [#429](https://github.com/fastapi/asyncer/pull/429) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.5 to 0.14.10. PR [#436](https://github.com/fastapi/asyncer/pull/436) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/download-artifact from 6 to 7. PR [#430](https://github.com/fastapi/asyncer/pull/430) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/upload-artifact from 5 to 6. PR [#431](https://github.com/fastapi/asyncer/pull/431) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.7.0 to 9.7.1. PR [#433](https://github.com/fastapi/asyncer/pull/433) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update secrets check. PR [#446](https://github.com/fastapi/asyncer/pull/446) by [@YuriiMotov](https://github.com/YuriiMotov).
* 🔧 Migrate from Material for MkDocs to Zensical. PR [#445](https://github.com/fastapi/asyncer/pull/445) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update pre-commit to use local Ruff instead of hook, unpin `prek`. PR [#443](https://github.com/fastapi/asyncer/pull/443) by [@YuriiMotov](https://github.com/YuriiMotov).

## 0.0.12

### Breaking Changes

* ➖ Drop support for Python 3.8. PR [#441](https://github.com/fastapi/asyncer/pull/441) by [@tiangolo](https://github.com/tiangolo).

### Docs

* 📝 Update code examples to Python 3.9. PR [#442](https://github.com/fastapi/asyncer/pull/442) by [@YuriiMotov](https://github.com/YuriiMotov).
* 📝 Relax the warnings as I have been using Asyncer in production for a while (and other teams as well). PR [#424](https://github.com/fastapi/asyncer/pull/424) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆️ Use prek as a pre-commit alternative. PR [#437](https://github.com/fastapi/asyncer/pull/437) by [@YuriiMotov](https://github.com/YuriiMotov).
* 👷 Configure coverage, error on main tests, don't wait for Smokeshow. PR [#435](https://github.com/fastapi/asyncer/pull/435) by [@YuriiMotov](https://github.com/YuriiMotov).
* 👷 Run Smokeshow always, even on test failures. PR [#434](https://github.com/fastapi/asyncer/pull/434) by [@YuriiMotov](https://github.com/YuriiMotov).
* 🔥 Remove Material for MkDocs Insiders extra files. PR [#432](https://github.com/fastapi/asyncer/pull/432) by [@tiangolo](https://github.com/tiangolo).

## 0.0.11

### Fixes

* 📝 Add `sniffio` dependency to project requirements. PR [#421](https://github.com/fastapi/asyncer/pull/421) by [@jujumilk3](https://github.com/jujumilk3).

### Docs

* 📝 Update docs to use `markdown-include-variants`. PR [#419](https://github.com/fastapi/asyncer/pull/419) by [@YuriiMotov](https://github.com/YuriiMotov).
* 💅 Update CSS to explicitly use emoji font. PR [#420](https://github.com/fastapi/asyncer/pull/420) by [@tiangolo](https://github.com/tiangolo).

### Internal

* ⬆ Bump actions/checkout from 5 to 6. PR [#418](https://github.com/fastapi/asyncer/pull/418) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/latest-changes from 0.4.0 to 0.4.1. PR [#417](https://github.com/fastapi/asyncer/pull/417) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump actions/checkout from 5 to 6. PR [#411](https://github.com/fastapi/asyncer/pull/411) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Tweak pre-commit config in CI. PR [#415](https://github.com/fastapi/asyncer/pull/415) by [@tiangolo](https://github.com/tiangolo).
* 👷 Add pre-commit GitHub Action workflow. PR [#413](https://github.com/fastapi/asyncer/pull/413) by [@tiangolo](https://github.com/tiangolo).
* 💄 Use font Fira Code to fix display of Rich panels in docs in Windows. PR [#412](https://github.com/fastapi/asyncer/pull/412) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Upgrade Material for MkDocs and remove insiders. PR [#410](https://github.com/fastapi/asyncer/pull/410) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump mkdocs-macros-plugin from 1.4.1 to 1.5.0. PR [#407](https://github.com/fastapi/asyncer/pull/407) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.6.23 to 9.7.0. PR [#406](https://github.com/fastapi/asyncer/pull/406) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.4 to 0.14.5. PR [#408](https://github.com/fastapi/asyncer/pull/408) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#409](https://github.com/fastapi/asyncer/pull/409) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.14.3 to 0.14.4. PR [#404](https://github.com/fastapi/asyncer/pull/404) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#405](https://github.com/fastapi/asyncer/pull/405) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mkdocs-material from 9.6.22 to 9.6.23. PR [#402](https://github.com/fastapi/asyncer/pull/402) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.2 to 0.14.3. PR [#401](https://github.com/fastapi/asyncer/pull/401) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#403](https://github.com/fastapi/asyncer/pull/403) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/upload-artifact from 4 to 5. PR [#397](https://github.com/fastapi/asyncer/pull/397) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-macros-plugin from 1.4.0 to 1.4.1. PR [#398](https://github.com/fastapi/asyncer/pull/398) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/download-artifact from 5 to 6. PR [#399](https://github.com/fastapi/asyncer/pull/399) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.14.1 to 0.14.2. PR [#394](https://github.com/fastapi/asyncer/pull/394) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#400](https://github.com/fastapi/asyncer/pull/400) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 🔧 Add PEP-639 license metadata. PR [#395](https://github.com/fastapi/asyncer/pull/395) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump typer from 0.19.2 to 0.20.0. PR [#393](https://github.com/fastapi/asyncer/pull/393) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.6.21 to 9.6.22. PR [#389](https://github.com/fastapi/asyncer/pull/389) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Configure reminder for `waiting` label in `issue-manager`. PR [#390](https://github.com/fastapi/asyncer/pull/390) by [@YuriiMotov](https://github.com/YuriiMotov).
* ⬆ Bump ruff from 0.13.3 to 0.14.1. PR [#391](https://github.com/fastapi/asyncer/pull/391) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#388](https://github.com/fastapi/asyncer/pull/388) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).

## 0.0.10

### Upgrades

* ⬆️ Add support for Python 3.14. PR [#387](https://github.com/fastapi/asyncer/pull/387) by [@svlandeg](https://github.com/svlandeg).

### Internal

* ⬆ Bump astral-sh/setup-uv from 6 to 7. PR [#386](https://github.com/fastapi/asyncer/pull/386) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.13.2 to 0.13.3. PR [#383](https://github.com/fastapi/asyncer/pull/383) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#384](https://github.com/fastapi/asyncer/pull/384) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mkdocs-macros-plugin from 1.3.9 to 1.4.0. PR [#373](https://github.com/fastapi/asyncer/pull/373) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.17.4 to 0.19.2. PR [#374](https://github.com/fastapi/asyncer/pull/374) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-material from 9.6.20 to 9.6.21. PR [#379](https://github.com/fastapi/asyncer/pull/379) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/issue-manager from 0.5.1 to 0.6.0. PR [#380](https://github.com/fastapi/asyncer/pull/380) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#372](https://github.com/fastapi/asyncer/pull/372) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.13.0 to 0.13.2. PR [#376](https://github.com/fastapi/asyncer/pull/376) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Update docs previews comment, single comment, add failure status. PR [#377](https://github.com/fastapi/asyncer/pull/377) by [@tiangolo](https://github.com/tiangolo).

## 0.0.9

### Fixes

* 👽️ Ensure compatibility with AnyIO 4.11.0. PR [#381](https://github.com/fastapi/asyncer/pull/381) by [@svlandeg](https://github.com/svlandeg).

### Docs

* 🩺 Take the GH badge only from pushes to the `main` branch. PR [#284](https://github.com/fastapi/asyncer/pull/284) by [@svlandeg](https://github.com/svlandeg).

### Internal

* 🔥 Remove unused Poetry config file. PR [#382](https://github.com/fastapi/asyncer/pull/382) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump mkdocs-material from 9.5.44 to 9.6.20. PR [#368](https://github.com/fastapi/asyncer/pull/368) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump astral-sh/setup-uv from 5 to 6. PR [#318](https://github.com/fastapi/asyncer/pull/318) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/download-artifact from 4 to 5. PR [#346](https://github.com/fastapi/asyncer/pull/346) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.12.12 to 0.13.0. PR [#367](https://github.com/fastapi/asyncer/pull/367) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#369](https://github.com/fastapi/asyncer/pull/369) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#366](https://github.com/fastapi/asyncer/pull/366) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/setup-python from 5 to 6. PR [#360](https://github.com/fastapi/asyncer/pull/360) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/labeler from 5 to 6. PR [#363](https://github.com/fastapi/asyncer/pull/363) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.17.3 to 0.17.4. PR [#364](https://github.com/fastapi/asyncer/pull/364) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.12.10 to 0.12.12. PR [#362](https://github.com/fastapi/asyncer/pull/362) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#357](https://github.com/fastapi/asyncer/pull/357) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump typer from 0.16.1 to 0.17.3. PR [#358](https://github.com/fastapi/asyncer/pull/358) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.12.4 to 1.13.0. PR [#359](https://github.com/fastapi/asyncer/pull/359) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Detect and label merge conflicts on PRs automatically. PR [#361](https://github.com/fastapi/asyncer/pull/361) by [@svlandeg](https://github.com/svlandeg).
* ⬆ Bump ruff from 0.12.9 to 0.12.10. PR [#354](https://github.com/fastapi/asyncer/pull/354) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#355](https://github.com/fastapi/asyncer/pull/355) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mkdocs-macros-plugin from 1.3.7 to 1.3.9. PR [#349](https://github.com/fastapi/asyncer/pull/349) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 4 to 5. PR [#348](https://github.com/fastapi/asyncer/pull/348) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 11.2.1 to 11.3.0. PR [#338](https://github.com/fastapi/asyncer/pull/338) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/latest-changes from 0.3.2 to 0.4.0. PR [#345](https://github.com/fastapi/asyncer/pull/345) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.16.0 to 0.16.1. PR [#352](https://github.com/fastapi/asyncer/pull/352) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.11.13 to 0.12.9. PR [#350](https://github.com/fastapi/asyncer/pull/350) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#335](https://github.com/fastapi/asyncer/pull/335) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#309](https://github.com/fastapi/asyncer/pull/309) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump pillow from 11.1.0 to 11.2.1. PR [#315](https://github.com/fastapi/asyncer/pull/315) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump cairosvg from 2.7.1 to 2.8.2. PR [#327](https://github.com/fastapi/asyncer/pull/327) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.15.2 to 0.16.0. PR [#331](https://github.com/fastapi/asyncer/pull/331) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.11.0 to 0.11.13. PR [#333](https://github.com/fastapi/asyncer/pull/333) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 🔧 Remove Google Analytics. PR [#329](https://github.com/fastapi/asyncer/pull/329) by [@tiangolo](https://github.com/tiangolo).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#306](https://github.com/fastapi/asyncer/pull/306) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.9.10 to 0.11.0. PR [#304](https://github.com/fastapi/asyncer/pull/304) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#301](https://github.com/fastapi/asyncer/pull/301) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.9.9 to 0.9.10. PR [#300](https://github.com/fastapi/asyncer/pull/300) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.15.1 to 0.15.2. PR [#299](https://github.com/fastapi/asyncer/pull/299) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump typer from 0.12.5 to 0.15.1. PR [#286](https://github.com/fastapi/asyncer/pull/286) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#298](https://github.com/fastapi/asyncer/pull/298) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump ruff from 0.9.7 to 0.9.9. PR [#296](https://github.com/fastapi/asyncer/pull/296) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.9.6 to 0.9.7. PR [#294](https://github.com/fastapi/asyncer/pull/294) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#295](https://github.com/fastapi/asyncer/pull/295) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump mypy from 1.11.2 to 1.14.1. PR [#276](https://github.com/fastapi/asyncer/pull/276) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.8.3 to 0.9.6. PR [#291](https://github.com/fastapi/asyncer/pull/291) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#290](https://github.com/fastapi/asyncer/pull/290) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Update httpx requirement from <0.28.0,>=0.27.0 to >=0.27.0,<0.29.0. PR [#288](https://github.com/fastapi/asyncer/pull/288) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump astral-sh/setup-uv from 3 to 5. PR [#273](https://github.com/fastapi/asyncer/pull/273) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump mkdocs-macros-plugin from 1.2.0 to 1.3.7. PR [#252](https://github.com/fastapi/asyncer/pull/252) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Update pre-commit requirement from <4.0.0,>=2.17.0 to >=2.17.0,<5.0.0. PR [#237](https://github.com/fastapi/asyncer/pull/237) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#275](https://github.com/fastapi/asyncer/pull/275) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump pypa/gh-action-pypi-publish from 1.10.1 to 1.12.4. PR [#280](https://github.com/fastapi/asyncer/pull/280) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump pillow from 10.4.0 to 11.1.0. PR [#277](https://github.com/fastapi/asyncer/pull/277) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump tiangolo/latest-changes from 0.3.1 to 0.3.2. PR [#261](https://github.com/fastapi/asyncer/pull/261) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump ruff from 0.6.5 to 0.8.3. PR [#271](https://github.com/fastapi/asyncer/pull/271) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#222](https://github.com/fastapi/asyncer/pull/222) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 🔨 Update docs previews script. PR [#267](https://github.com/fastapi/asyncer/pull/267) by [@tiangolo](https://github.com/tiangolo).
* 🔧 Update build-docs filter paths. PR [#266](https://github.com/fastapi/asyncer/pull/266) by [@tiangolo](https://github.com/tiangolo).
* ⬆ Bump mkdocs-material from 9.5.34 to 9.5.44. PR [#257](https://github.com/fastapi/asyncer/pull/257) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Fix smokeshow, checkout files on CI. PR [#243](https://github.com/fastapi/asyncer/pull/243) by [@tiangolo](https://github.com/tiangolo).
* 👷 Use uv for CI. PR [#242](https://github.com/fastapi/asyncer/pull/242) by [@tiangolo](https://github.com/tiangolo).
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
