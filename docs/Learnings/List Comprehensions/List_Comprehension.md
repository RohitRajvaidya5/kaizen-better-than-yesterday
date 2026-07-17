# List Comprehension

## What is List Comprehension?

List comprehension is a concise and Pythonic way to create a new list by iterating over an iterable. It can also transform items and optionally filter them using a condition, making the code shorter and more readable than a traditional `for` loop.

Use list comprehensions when you're creating a new list from an existing iterable.

---

## Traditional `for` Loop

```python
numbers = []

for i in range(5):
    numbers.append(i)
```

---

## With List Comprehension

```python
numbers = [i for i in range(5)]
```

---

## When to Use List Comprehension

Use a list comprehension when you can describe your task like this:

> "Create a new list by taking every item, optionally filtering some items, and transforming the remaining items."

If you find yourself writing multiple `if` statements, nested loops, or performing actions instead of building a list, switch to a regular `for` loop.

---

## Interview Tip

For Python backend interviews (especially at product companies), list comprehensions are expected knowledge. You should be comfortable writing them for:

- Extracting fields from dictionaries
- Filtering records
- Transforming API or database results
- Simple nested iterations
- Combining filtering and transformation

They are widely used in Django, FastAPI, data processing, and general Python code, so being fluent with them will make both your interview solutions and production code cleaner.
