def fizzBuzz(num):
    ret = ""
    if isMultiple(num, 3): ret += "Fizz"
    if isMultiple(num, 5): ret += "Buzz"
    if not ret: ret = f"{num}"
    return ret

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


for i in range(21):
    print(fizzBuzz(i + 1))
