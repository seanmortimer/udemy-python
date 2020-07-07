import pytest

def fizzBuzz(num):
    result = ""
    if isMultiple(num, 3): result += "Fizz"
    if isMultiple(num, 5): result += "Buzz"
    if not result: result = f"{num}"
    return result

# utility fn for DRY
def isMultiple(num, mod):
    return (num % mod) == 0

# utility fn to improve DRY
def checkFizzBuzz(num, expected):
    result = fizzBuzz(num)
    assert result == expected
def test_returns1WhenPassed1():
    checkFizzBuzz(1, "1")

def test_return2With2():
    checkFizzBuzz(2, "2")


def test_FizzWith3():
    checkFizzBuzz(3, "Fizz")

def test_BuzzWith5():
    checkFizzBuzz(5, "Buzz")
    
def test_FizzWith6():
    checkFizzBuzz(6, "Fizz")

def testBuzzWith10():
    checkFizzBuzz(10, "Buzz")

def testFizzBuzz15():
    checkFizzBuzz(15, "FizzBuzz") 


# for i in range(21):
#     print(fizzBuzz(i + 1))


@pytest.fixture(params=[3, 6, 9, 12, 18, 21, 24])
def setup(request):
    result = request.param
    print(f"\nSetup Fizz... {result}")
    return result

def test_Fizzes(setup): 
    print(f"param {fizzBuzz(setup)}")
    checkFizzBuzz(setup, "Fizz")