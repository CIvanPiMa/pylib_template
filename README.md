# Python Library Template

```shell
cookiecutter git@github.com:CIvanPiMa/pylib_template.git
```

## Features

- [setuptools](https://setuptools.readthedocs.io/en/latest/) for packaging.
- Use of [pyproject.toml](https://pep-518.readthedocs.io/en/latest/) to manage the project.
- [pdoc](https://pdoc3.github.io/pdoc/) for documentation generation and deployment to GitHub Pages.
- [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html)  to manage the versioning, changelog and release process with:
  - [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) and
  - [semantic versioning](https://semver.org/).
- Code style and linting (configured with [pre-commit](https://pre-commit.com/) hooks):
  - [ruff](https://ruff.readthedocs.io/en/latest/)
  - [mypy](https://mypy.readthedocs.io/en/stable/)
- Testing and compatibility assurance (integrated with github actions):
  - [pytest](https://docs.pytest.org/en/stable/contents.html) for TDD or
  - [behave](https://behave.readthedocs.io/en/latest/index.html) for BDD
  - WIP: [tox](https://tox.readthedocs.io/en/latest/) for testing in multiple environments.
- [click](https://click.palletsprojects.com/en/8.0.x/) for command line interfaces.

TODO:

- [ ] Add TOX support and github actions
