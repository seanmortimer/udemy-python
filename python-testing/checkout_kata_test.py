import pytest
from checkout_kata import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout
    

def test_totalItems(checkout):
    checkout.addItem("a")
    assert checkout.totalItems() == 1

def test_total2Items(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.totalItems() == 3

def test_addDiscount(checkout):
    checkout.addDiscount("a", 3, 2)

def test_applyDiscount(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.totalItems() == 2 

def test_exceptionNoPrice(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")