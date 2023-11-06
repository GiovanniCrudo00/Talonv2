import pytest
from app.Validators import *
from app.CustomExceptions import *
import warnings


@pytest.fixture(autouse=True)
def disable_warnings():
    warnings.simplefilter("ignore")
    
def test_long_domain_name_raises_DomainNotValid_exception(): # Maximum 100 chars
    with pytest.raises(DomainNotValid):
        ValidateTargetDomain("a"*100)

def test_domain_of_at_maximum_99_chars_but_invalid_domain_given_raises_DomainNotValid():
    with pytest.raises(DomainNotValid):
        ValidateTargetDomain("a"*99)

@pytest.mark.parametrize("target",[
    ("notADomain"),
    ("notadomain"),
    ("-.com"),
    (None)
])
def test_invalid_domain_raises_exception_DomainNotValid(target):
    with pytest.raises(DomainNotValid):
        ValidateTargetDomain(target)

@pytest.mark.parametrize("target",[
    ("example.com"),
    ("xn--stackoverflow.com"),
    ("stackoverflow.xn--com"),
    ("stackoverflow.co.uk")
])
def test_valid_domains_is_returned_by_ValidateTargetDomain(target):
    assert target == ValidateTargetDomain(target)

@pytest.mark.parametrize("target",[
    ("3.4.5"),
    ("abcd"),
    ("notip.com"),
    (None),
    ("256.256.256.256")
])
def test_invalid_IP_raises_exception_IPNotValid(target):
    with pytest.raises(IPNotValid):
        ValidateTargetIP(target)

@pytest.mark.parametrize("target",[
    ("10.0.0.1"),
    ("1.1.1.1"),
    ("192.168.168.168")
])
def test_valid_IP_is_returned_by_ValidateTargetIP(target):
    assert target == ValidateTargetIP(target)