# Python Library Template

```shell
cookiecutter git@github.com:CIvanPiMa/pylib_template.git
```

## Features

- `Setuptools` as build engine
- Use of `pyproject.toml` to manage the project
- `Click` for the CLI implementation
- `pdoc` for easy documentation generation
- Support for semantic versioning with `bump-my-version`
- Code style and linting (configured with pre-commit hooks)
  - `ruff`
  - `mypy`
- For testing and compatibility assurance
  - `pytest` or `behave`
  - `tox`

# TODOs

- [ ] Add pre commit hook to ensure use of conventional commits
- [ ] Implement github actions to:
  - [ ] Use semver to bump the version in CI/CD pipelines
  - [ ] Use conventional commits to compute the next version
  - [ ] Autofill the CHANGELOG.md from the commit messages
