from typing import Union
import unicodedata

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    return a + b

def subtract(a: Number, b: Number) -> Number:
    return a - b

def multiply(a: Number, b: Number) -> Number:
    return a * b

def divide(a: Number, b: Number) -> Number:
    return a / b

def factorial(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)

def reverse_words(s: str) -> str:
    words = s.split(" ")
    words.reverse()
    return unicodedata.normalize("NFD", " ".join(words))