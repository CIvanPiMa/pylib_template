Feature: Say hello!

    Scenario: Run the cli command
        Given I have the cli installed
        When I run the 'hello' command with '{{ cookiecutter.full_name }}' as argument
        Then I should see 'Hello {{ cookiecutter.full_name }}!'
