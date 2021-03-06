"""Python for Visual Effects.

Assignment #1 - Data Types and Variables

Answer the following questions.
"""

# 1.- Make a program that solves and shows the summation of 64 + 32
print(64+32)

# 2.- Do the same as the question one but this time use variables instead of 
# numbers.
number1 = 64
number2 = 32
print(number1 + number2)

# 3.- Make a program that prints a sentence that includes at least 3 variables.
name = "Onur Can Yol"
school = "Seneca College"
age = "23"
print("My name is " + name + ", i am studying at " + school + " and i am " + age + " years old.")

# 4.- Given a sentence, assign the string to a variable then print the number of 
# characters in the sentence. 
# The sentence is "This is my first Python program."
sentence = "This is my first Python program."
print(len(sentence))

# 5.- Given the resolution 1920 x 1080, make a program that prints a string with 
# the 10% over-scan value of those numbers. The printed string must be as 
# follows: "The 10% overscan of 1920 is <value 1>, and the 1080 is <value 2>"
width = 1920
height = 1080
value_1 = (str(int(width + width*0.1)))
value_2 = (str(int(height + height*0.1)))
result = "The 10% overscan of 1920 is " + value_1 + " and the 1080 is " + value_2 + "."
print(result)