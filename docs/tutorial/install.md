# Install

The first step is to set up your project and add **Asyncer**.

Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/), then create a project and add Asyncer:

<div class="termy">

```console
$ uv init awesome-project --bare
$ cd awesome-project
$ uv add asyncer
---> 100%
```

</div>

`uv add` creates the project's virtual environment in `.venv`, adds Asyncer to `pyproject.toml`, and creates `uv.lock` so the same package versions can be installed later.

/// details | What these commands do

* `uv init`: create a new Python project.
* `awesome-project`: create the project in a new directory with this name.
* `--bare`: create only the minimal `pyproject.toml` file, without generating a sample `main.py`, `README.md`, or other files. You will create the application files yourself in the next steps of this tutorial.

Then `cd awesome-project` enters the new project directory before adding Asyncer.

`uv` will use a compatible Python version already installed on your system, or download one if needed.

When you run `uv add`, it selects compatible versions of Asyncer and all the packages Asyncer depends on. It records the exact versions in `uv.lock`, making it possible to install the same package versions later on another computer.

Creating or updating this file is called [**locking** the project dependencies](https://docs.astral.sh/uv/concepts/projects/sync/). `uv` does this automatically when you add a package.

///

/// details | Using `pip` instead

If you prefer to manage a virtual environment and packages manually, create and activate a virtual environment and then install Asyncer with `pip install asyncer`.

Read the [Virtual Environments guide](https://tiangolo.com/guides/virtual-environments/) for the detailed steps.

///
