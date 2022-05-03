#tests

from cgi import test
from app.college_data import to_usd, to_pct, get_data

def test_usd():
    assert to_usd(75,000) == "$75,000"

def test_pct():
    assert to_pct(0.12) == "12%"

def data_test():
    assert type(get_data("georgetown university")) == dict
