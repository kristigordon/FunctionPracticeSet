# def even_calc(number):
#     if number % 2 == 0:
#         return True
#      return False

# def is_even(num):
#     return num % 2 == 0

# def slugify(phrase):
#     return phrase.lower().strip().replace(" ", "-")

from itertools import count


def count_vowels(phrase):
    count = 0
    for char in phrase:
        if char in "aeiou":
            count += 1 
    return count

print(count_vowels("hello world"))