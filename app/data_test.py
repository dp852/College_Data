#tests
import os
from cgi import test
from app.college_data import to_usd, to_pct, get_data

CI_ENV = os.getenv("CI") == "true"

def test_usd():
    assert to_usd(75000) == "$75,000.00"

def test_pct():
    assert to_pct(0.12) == "12.00%"

def dict_test():
    assert type(get_data("georgetown university")) == dict
