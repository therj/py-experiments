# Question 1
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

name = input('Enter your name: ')
age = input('Enter your age: ')

age = int(age)

age_to_100 = 100 - age

print(f"{name}, you'll turn 100 in {age_to_100} years")
