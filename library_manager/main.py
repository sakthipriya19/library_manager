# main.py
from models import LibraryItem, Book, Magazine, DVD, Member

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Monthly", 2, 42)
dvd = DVD("Planet Earth", 3, 120)
extra_book = Book("Clean Code", 4, "R. Martin")

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# 0. The abstract parent cannot be created directly
print("=== Abstract class ===")
try:
    LibraryItem("x", 1)
except TypeError as e:
    print("Cannot create LibraryItem:", e)

# 1. Borrowing with error handling
print("\n=== Borrowing ===")
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
    bob.borrow(book)  # should fail: already borrowed
except ValueError as e:
    print("Could not borrow:", e)

# 2. Borrow-limit error and not-borrowed error
print("\n=== Borrow limit ===")
try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # should fail: Bob's limit is 1
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.borrow(dvd)
    alice.borrow(extra_book)
    print("Alice now has:", alice.borrowed_titles())
    alice.borrow(Book("Extra Reading", 5, "S. Iyer"))  # 4th item: over the default limit of 3
except ValueError as e:
    print("Could not borrow:", e)

print("\n=== Returning ===")
try:
    fee = alice.return_item(book, days_late=4)
    print(f"Alice returned '{book.title}' 4 days late. Fee: Rs {fee}")
    alice.return_item(magazine)  # should fail: Bob has it, not Alice
except ValueError as e:
    print("Could not return:", e)

try:
    alice.return_item(book)  # should fail: already returned
except ValueError as e:
    print("Could not return:", e)

fee = bob.return_item(magazine)
print(f"Bob returned '{magazine.title}' on time. Fee: Rs {fee}")
print("Alice now has:", alice.borrowed_titles())
print("Bob now has:", bob.borrowed_titles())

# 3. Polymorphism: one loop, no type checks
print("\n=== Late fees (polymorphism) ===")
items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))

# 4. Encapsulation: the private attribute is hidden from outside code
print("\n=== Encapsulation ===")
try:
    print(dvd.__available)
except AttributeError as e:
    print("Direct access failed:", e)
print(f"Is '{dvd.title}' available? {dvd.is_available()}")
print(f"Is '{book.title}' available? {book.is_available()}")

# 5. Class attribute shared by all objects
print("\n=== Class attribute ===")
print("Total items created:", Book.total_items)
print("Same value via LibraryItem:", LibraryItem.total_items)
