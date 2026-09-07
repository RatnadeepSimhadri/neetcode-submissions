from typing import List

def contains_duplicate(words: List[str]) -> bool:
    unique_words = set(words)
    return True if len(words) != len(unique_words) else False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
