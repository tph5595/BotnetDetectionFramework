""" test: used to test the other files in this project """
# Testing framework
import pytest

# Files to be tested


@pytest.mark.parametrize("num, ans", [(4, 8)])
def test_dummy(num, ans, debug=False):
    """Dummy test for CICD"""
    assert ans == (num * 2)
