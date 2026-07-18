# Optional Keyword


```python

from typing import Optional

def greet(name: Optional[str]):

    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")


greet("Rohit") -->  Output : Hello Rohit


def create_user(name: str, age: Optional[int] = None):
    print(name, age)

create_user("Max", 27) --> Max 27

class User:
    def __init__(self):
        self.email: Optional[str] = None


def greet2(name : str | None):

    return f"Hi + {name}"



```


**Optional** is one of the keywords used in the typing module.

Mostly it is used for code readability and better debugging and something like that.

If we use Optional like this:

```python

def greet(name: Optional[str])

```


That does not mean Optional will check if the name is a string or not.

It is just a metadata provided to the function which increases code readability.
It is not enforceable at runtime.

Mostly Optional is used in Python versions below 3.10.

With Python 3.10 and above, the same thing is written like this:

```python

def greet(name: str | None)

```

> So maybe if Python 3.9 and lower versions get deprecated,
> Optional can also get deprecated in the future.
