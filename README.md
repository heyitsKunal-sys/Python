# 🐍 Python Learning Roadmap – From Basics to Advanced

## 📌 Overview

This repository documents a complete and structured  to mastering Python — starting from fundamental concepts to advanced programming techniques. It is designed for beginners as well as developers aiming to strengthen their core understanding and practical skills in Python.

---

## 🧠 1. Fundamentals of Python

### 🔹 Variables

* Definition and declaration
* Naming conventions
* Dynamic typing

```python
x = 10
name = "Kunal"
```

### 🔹 Data Types

* **Primitive Types**: `int`, `float`, `complex`, `bool`, `str`
* **Collection Types**: `list`, `tuple`, `set`, `dict`

```python
a = 10          # int
b = 3.14        # float
c = "Hello"     # string
d = True        # boolean
```

---

## 🔄 2. Control Flow

### 🔹 Conditional Statements

```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### 🔹 Loops

* `for` loop
* `while` loop
* Loop control: `break`, `continue`, `pass`

---

## 📦 3. Data Structures

### 🔹 Lists

* Mutable, ordered collection

### 🔹 Tuples

* Immutable, ordered collection

### 🔹 Sets

* Unordered, unique elements

### 🔹 Dictionaries

* Key-value pairs

```python
my_dict = {"name": "Kunal", "age": 21}
```

---

## 🧩 4. Functions

### 🔹 Function Basics

```python
def greet(name):
    return f"Hello {name}"
```

### 🔹 Types of Functions

* Built-in functions
* User-defined functions
* Recursive functions
* Lambda functions

---

## ⚡ 5. Advanced Functions

### 🔹 Lambda Functions

```python
square = lambda x: x * x
```

### 🔹 Map Function

```python
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
```

### 🔹 Filter Function

```python
nums = [1, 2, 3, 4]
result = list(filter(lambda x: x % 2 == 0, nums))
```

### 🔹 Reduce Function

```python
from functools import reduce
result = reduce(lambda x, y: x + y, nums)
```

---

## 🧱 6. Object-Oriented Programming (OOP)

### 🔹 Classes & Objects

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### 🔹 Key Concepts

* Encapsulation
* Inheritance
* Polymorphism
* Abstraction

---

## 📁 7. File Handling

```python
with open("file.txt", "r") as f:
    content = f.read()
```

* Modes: `r`, `w`, `a`, `rb`, `wb`

---

## 📦 8. Modules & Packages

* Importing modules
* Creating custom modules

```python
import math
print(math.sqrt(16))
```

---

## ⚙️ 9. Exception Handling

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error occurred")
finally:
    print("Execution completed")
```

---

## 🔄 10. Iterators & Generators

### 🔹 Iterators

* `__iter__()` and `__next__()`

### 🔹 Generators

```python
def count(n):
    for i in range(n):
        yield i
```

---

## 🧪 11. Advanced Python Concepts

* Decorators
* Context Managers
* List/Dict Comprehensions
* Multithreading & Multiprocessing
* Virtual Environments

---


Consistency is key. Practice daily, build projects, and gradually move from basics to advanced topics.

Happy Coding! 🐍
