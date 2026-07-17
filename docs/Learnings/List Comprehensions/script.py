# ----------------------------------------
# Transforming Data
# ----------------------------------------

numbers = [i for i in range(5)]

squares = [i ** 2 for i in range(6)]

names = ["rohit", "raj", "amit"]
upper_names = [name.upper() for name in names]

words = ["apple", "banana", "cat"]
lengths = [len(word) for word in words]

# ----------------------------------------
# Filtering Data
# ----------------------------------------

filtered_words = [
    word.upper()
    for word in words
    if word.startswith("a")
]

even_numbers = [
    n
    for n in range(1, 11)
    if n % 2 == 0
]

# ----------------------------------------
# Conditional Expressions
# ----------------------------------------

labels = [
    "Even" if n % 2 == 0 else "Odd"
    for n in range(1, 6)
]

# ----------------------------------------
# Practice Problems
# ----------------------------------------

numbers_1_to_20 = [n for n in range(1, 21)]

squares_1_to_10 = [n ** 2 for n in range(1, 11)]

text = "rohit rajvaidya"

vowels = [
    ch
    for ch in text
    if ch.lower() in "aeiou"
]

upper_words = ["APPLE", "BANANA", "CARROT", "MANGO"]

lower_words = [
    word.lower()
    for word in upper_words
]

negative_numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

non_negative_numbers = [
    n if n > 0 else 0
    for n in negative_numbers
]

print(non_negative_numbers)
