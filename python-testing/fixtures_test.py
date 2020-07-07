import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup now")

@pytest.mark.test1
def test1():
# def test1(setup): <-- for not using autouse
    print("Executing test1")
    assert True

# @pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2")
    assert True
    

# yield and addfinalizer are used for teardown with fixtures
# they run when the fixture goes out of scope


# params run tests with each value in the param array
@pytest.fixture(params=[1, 2, 3])
def setup2(request):
    result = request.param
    print(f"\nSetup...  result = {result}")
    return result

def test3(setup2):
    print("\nsetup = {}".format(setup2))
    assert True
    

# Approx can be used for comparing floats and such:
def test_badTest():
     assert (0.1 + 0.2) != 0.3 

def test_goodTest():
    assert (0.1 + 0.2) == pytest.approx(0.3)


# checking for raised errors
def raiseValueException():
    raise ValueError
      
def test_exception():
    with pytest.raises(ValueError):
        raiseValueException()