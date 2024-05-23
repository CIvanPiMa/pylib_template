# First steps

**GitHub**:

- Create a [new repository](https://github.com/new) with the name `{{cookiecutter.repo_name}}`.
- Enable the **doc** generation in the repository:
  - Settings -> Pages -> Source: Github Actions

**Local**:

- Initialize the repository:

```shell
git init --initial-branch={{cookiecutter.main_branch}}
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:{{cookiecutter.repo_path}}.git
git push -u origin {{cookiecutter.main_branch}}
```

- Use and push a development branch:

```shell
BRANCH_NAME=feat/initial_project_release
git checkout -b ${BRANCH_NAME}
git add .
git commit -m "feat: Add initial project structure"
git push --set-upstream origin ${BRANCH_NAME}
```

- Install the pre-commit hooks:

```shell
pre-commit install --install-hooks --hook-type commit-msg
```

---

# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

- [Docs](https://{{ cookiecutter.username.lower() }}.github.io/{{ cookiecutter.repo_name }}/{{ cookiecutter.repo_name }}.html).

## Installation

```shell
pip install {{cookiecutter.repo_name}}
```

## Usage

...TBD

## Contributing

Once cloned the repo, install the [pre-commit](https://pre-commit.com/#install) hooks:

```shell
pre-commit install --install-hooks --hook-type commit-msg
```

Install the library (in a virtual environment) as an editable package with the development dependencies:

```shell
pip install -e ".[dev]"
```

### Documentation

- This library uses the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format for the docstrings.
- To generate the documentation, run:

```shell
pdoc src/{{cookiecutter.repo_name}} --mermaid --docformat numpy
```

### Testing

To run the tests:

{% if cookiecutter.testing == "TDD" -%}
```shell
pytest
```
{%- elif cookiecutter.testing == "BDD" -%}
```shell
behave
```
{%- endif %}
