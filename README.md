# FunctionPracticeSet

Practicing Functions with default parameters.

```
def even_calc(number):
    if number % 2 == 0:
        return True
     return False

def is_even(num):
    return num % 2 == 0

def slugify(phrase):
    return phrase.lower().strip().replace(" ", "-")


def count_vowels(phrase):
    count = 0
    for char in phrase:
        if char in "aeiou":
            count += 1 
    return count

# print(count_vowels("hello world"))

#We can give our function default parameters
def laugh(intensity=10)
    print("HA" * intensity)

#can call laugh and enter a parameter
laugh(10)
#and it would be 10
#or call the function without a parameter 
laugh()
#and you won't get an error, it will default to 2 
#so if you provide a value, it is still used, but if you don't, it defaults to the given parameter
 
#You can also do this with our previous function
def slugify(phrase, sep="-"):
    return phrase.lower().strip().replace(" ", sep)

#Now if you provide a value, it will be used, but if you don't, it defaults to the given parameter sep - 
#You cannot have a default value before an parameter, any default values need to come last.

def greet(msg="hi", person)
    print(f"{msg}, {person}!!!")
greet("Jace")
#The computer doesn't know if this changes the default value for msg or if it is for person. It will change the default then have nothing for the remaining parameter and throw an error. 
#This will produce an error message but this next one will not
def greet(person, msg="hi")
    print(f"{msg}, {person}!!!")
greet("Jace")
#You can still call them in whatever order you would like, but they just have to be initially set up this way.
```
