# Pytest expects certain conventions for easy test discover
# Name the file with your tests for a specific module
# "test_module" or "module_test" in case it has trouble finding them

# In order to write tests with pytest, I need to import at least two things
# 1. pytest itself
# 2. The code from the module you are testing

# Unit tests directly call the code under test.
# This introduces som econsiderations when your code talks to other outside systems
# like APIs or DBs.

import pytest
from calculator import add, subtract, multiply, divide

# within our test.py module, we want to keep respecting naming conventions
# THese are just python methods, but we name them as follows
# test_(method_name)_(what_you_are_looking_for)
def test_divide_success():

    # UNit tests generally follow A-A-A pattern
    # Arrange, act, assert

    # Arrange - any variables or test data we need to set up is created in this step
    x = 4
    y = 2

    # ACT - here is where we actually call the code under test
    result = divide(x, y)

    # Assert - We know what data we fed in, we know what we should get back
    # We assert that we got our expected result back
    assert result ==2

def test_divide_divide_by_zero_exception():

    # Arrange
    x = 400
    y = 0 # Intentional divide by 0

    # Act - Assert

    with pytest.raises(ValueError) as ex:
        divide(x, y)

    # Casting ex.value as a string, to allow for easy comparison
    assert str(ex.value) == "Cannot divide by zero"

def test_add():
    # Arrange
    x = 4
    y = 6

    # Act
    result = add(x, y)

    # Assert
    assert result == 10
