import subprocess


def test_main():
    assert subprocess.check_output(["{{cookiecutter.repo_name}}_cli", "hello", "--name", "{{cookiecutter.full_name}}"], text=True) == "Hello {{cookiecutter.full_name}}!\n"
