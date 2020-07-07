import pytest
from checkout_kata import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout
    

def test_canAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)

def test_canAddItem(checkout):
    checkout.addItem("a")