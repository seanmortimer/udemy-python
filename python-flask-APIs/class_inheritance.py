class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer1", "USB", 500)
printer.print(25)
print(printer)
printer.disconnect()
printer.print(50)

print("")
# Class composition > recommended over inheritance

class Bookshelf:
    def __init__(self, *books):
        self.books = books
        
    def __str__(self):
        return f"Bookshelf has {len(self.books)} books."

# shelf = Bookshelf(500)

# print(shelf)


class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("How to Python")
shelf = Bookshelf(book, book2)

print(book)
print(book2)
print(shelf)
print(shelf.books)
