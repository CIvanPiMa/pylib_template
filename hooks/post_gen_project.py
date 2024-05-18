"""
This script is executed after the project has been generated.
It removes the `features` directory if the test type is TDD
Or it removes the `tests` directory if the test type is BDD
"""

import os
import shutil

WORKING_DIR = os.getcwd()
PROJECT_DIR = f"{WORKING_DIR}/src/{{cookiecutter.repo_name}}"
TESTS_DIR = f"{WORKING_DIR}/tests"


def remove(filepath: str):
    """
    Remove a file or directory
    """
    print(f"Removing: {filepath=}")
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


TEST_TYPE = "{{cookiecutter.testing}}"
if TEST_TYPE == "TDD":
    remove(os.path.join(WORKING_DIR, "features"))
    PROJECT_DIR = os.path.basename(WORKING_DIR)
elif TEST_TYPE == "BDD":
    remove(os.path.join(WORKING_DIR, "tests"))
    PROJECT_DIR = os.path.basename(WORKING_DIR)

IDE = "{{cookiecutter.ide}}"
if IDE != "vscode":
    remove(os.path.join(WORKING_DIR, ".vscode"))
    PROJECT_DIR = os.path.basename(WORKING_DIR)

CLI = "{{cookiecutter.use_cli}}"
if CLI == "no":
    remove(os.path.join(PROJECT_DIR, "cli.py"))
    remove(os.path.join(PROJECT_DIR, "__main__.py"))
    remove(os.path.join(TESTS_DIR, "test_cli.py"))

print("Project generated successfully!")
