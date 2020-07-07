# Type hinting (required Python > 3.5)
from typing import List

def list_avg(sequence: List) -> float:
    # sequence must be a list, function will return a float
    return sum(sequence) / len(sequence)

print(list_avg([1,2,3]))
print()


# Error handling
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by 0.")
            
    return dividend / divisor



grades = []
grades2 = [77, 88, 99]

def avg_grade(g):
    print("Average grade program.")
    try:
       average = divide(sum(g), len(g))
    except ZeroDivisionError as e:
        print(e)
        print("There are no grades yet.")
    else:
       print(f"The average grade is {average}.")
    finally:
        print("The program is complete.")
        print()
       
avg_grade(grades)
avg_grade(grades2)

# Custom error classes (with type hinting)
# You must inherit from an existing error in order to raise the custom error
class TooManyPagesError(ValueError):
    pass

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __str__(self):
        return(
            f"Book: {self.name}, read {self.pages_read} pages of {self.page_count}"
        )
    
    def read(self, pages: int):
        total_pages = self.pages_read + pages
        if total_pages > self.page_count:
            raise TooManyPagesError(
        f"<You tried to read {total_pages} pages, but {self.name} only has {self.page_count} pages.>"
        )
        self.pages_read += pages
        print(f"You have just read {pages} pages for a total of {self.pages_read}")

book1 = Book("The Hobbit", 100)
print(book1)
try:
    book1.read(50)
    book1.read(550)
except TooManyPagesError as e:
    print(e)

print(book1)
