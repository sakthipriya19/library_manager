# Library Manager

A small Python program for a campus library that lends books, magazines and DVDs. It stores items, lets members borrow and return them, works out late fees, and refuses invalid actions with clear messages instead of crashing.

## How to run

Requires Python 3.12 or later and no external packages.

```
python3 main.py      # on Windows: python main.py
```

The full console output of the final run is in `output.txt`.

## Files

- `models.py`: the abstract `LibraryItem` parent, its children `Book`, `Magazine` and `DVD`, and the `Member` class.
- `main.py`: a demo that uses every feature.
- `output.txt`: the output of `main.py`.

## Reflection

**1. Why is `LibraryItem` abstract, and what happens if `DVD` forgets to write `late_fee()`?**

`LibraryItem` is only a general idea. Every real item is a book, a magazine or a DVD, and each has its own daily rate, so there is no sensible late fee for a plain "item". Marking `late_fee()` with `@abstractmethod` makes it a rule that every child class must write its own version, and it stops anyone from creating a `LibraryItem` directly. If `DVD` left out `late_fee()`, `DVD` would also count as abstract, and `DVD("Planet Earth", 3, 120)` would raise a `TypeError` the moment you tried to create it. The mistake shows up straight away, not later when someone tries to charge a fee.

**2. What happens when you read `item.__available` from outside the class, and why do we use `is_available()` instead?**

You get an `AttributeError`. Python renames (name-mangles) any attribute that starts with two underscores to `_LibraryItem__available` inside the class, so `item.__available` doesn't exist from the outside. We call `is_available()` because it lets other code read the value without being able to change it. Availability then only changes through `mark_borrowed()` and `mark_returned()`, which `Member` calls as part of a proper borrow or return, so an item can never be marked as taken without being on a member's list.

**3. What is the difference between `LibraryItem.total_items` and `self.title`?**

`total_items` is a class attribute: the class holds one copy and every object shares it. That is why it counts all items created and gives the same answer whether you read it through `Book`, `LibraryItem` or any item. `self.title` is an instance attribute: each object has its own copy, set in `__init__`, so every book, magazine and DVD keeps its own title.
