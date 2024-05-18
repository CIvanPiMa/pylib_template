import pytest
from {{cookiecutter.repo_name}}.dog import Dog


@pytest.fixture
def coco() -> Dog:
    return Dog(name="Coco", friends=["Gorda", "Gordo"])

def test_woofs(coco: Dog):
    coco.bark() == "*WOOF* *WOOF* GORDA *WOOF* GORDO!!!"
