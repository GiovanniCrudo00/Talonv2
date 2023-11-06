import pytest 
import warnings


@pytest.fixture(autouse=True)
def disable_warnings():
    warnings.simplefilter("ignore")

def test_dummy():
    assert True