from importlib import import_module
import subprocess
from behave import given, when, then
from behave.runner import Context


@given("I have the cli installed")
def step_impl(context: Context):
    module = import_module("{{ cookiecutter.repo_name }}")
    assert module is not None


@when("I run the 'hello' command with '{{ cookiecutter.full_name }}' as argument")
def step_impl(context: Context):
    response = subprocess.check_output(["{{ cookiecutter.repo_name }}_cli", "hello", "--name", "{{ cookiecutter.full_name }}"], text=True)
    context.response = response


@then("I should see 'Hello {{ cookiecutter.full_name }}!'")
def step_impl(context: Context):
    assert context.response == "Hello {{ cookiecutter.full_name }}!\n"
    # assert False
