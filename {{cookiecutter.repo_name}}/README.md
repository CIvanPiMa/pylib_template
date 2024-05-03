# First steps

- Create a new repository on GitHub with the name `{{cookiecutter.repo_name}}`.

- Then run the following commands to initialize the repository:

```shell
git init --initial-branch={{cookiecutter.repo_main_branch}}
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:{{cookiecutter.repo_path}}/{{cookiecutter.repo_name}}.git
git push -u origin {{cookiecutter.repo_main_branch}}

```

- Finally, checkout to a development branch and push the initial project structure:

```shell
git checkout -b feat/first-release
git add .
git commit -m "feat: Add initial project structure"
git push --set-upstream origin ${BRANCH_NAME}
```

---

# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Installation

```shell
pip install {{cookiecutter.project_name}}
```

## Usage

...TBD

## Contributing

Once you pull the repo, install the pre-commit hooks:

```shell
pre-commit install --install-hooks
```

Install the library as editable with the development dependencies:

```shell
pip install -e ".[dev]"
```

And run the tests:

{%- if cookiecutter.testing == "TDD" %}
```shell
pytest
```
{%- elif cookiecutter.testing == "BDD" %}
```shell
behave
```
{%- endif -%}
