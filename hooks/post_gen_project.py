"""
This script is executed after the project has been generated.
It removes the `features` directory if the test type is TDD
Or it removes the `tests` directory if the test type is BDD
"""
import os
import shutil

CWD = os.getcwd()
TEST_TYPE = "{{cookiecutter.testing}}"


def remove(filepath: str):
    """
    Remove a file or directory
    """
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if TEST_TYPE == "TDD":
    remove(os.path.join(CWD, "features"))
elif TEST_TYPE == "BDD":
    remove(os.path.join(CWD, "tests"))
