"""
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

Once cloned the repo, install the pre-commit hooks:

```shell
pre-commit install --install-hooks
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

{%- if cookiecutter.testing == "TDD" %}
```shell
pytest
```
{%- elif cookiecutter.testing == "BDD" %}
```shell
behave
```
{%- endif %}
"""

__version__ = "{{cookiecutter.version}}"
