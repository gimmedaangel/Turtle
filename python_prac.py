import math
# variables
print("hello" * 10)       # string multiplication
print(10*10 + 10/2)      # arithmetic operations
print(10 % 3)  # divides two numbers but prints only the remainder
print(10 // 3)  # divides two numbers but prints only the whole number
print(2 ** 3)  # exponentiation - raises number to the power of another number

students_uni = 1000, 2000, 3000

average_grade = 5.5             # Float

male_students = True            # Boolean
female_students = False         # Boolean

students_name = 'Roman'
food = "chicken"       # String

email_massage = """
Hello, Man

How are ya doing?
"""                     # Multiline String

print(len(students_name))   # len() function - length of string

print(food[0])          # indexing - first letter of string
print(food[-1])         # indexing - last letter of string
print(food[0:3])       # slicing - first 3 letters of string
print(food[:])         # slicing - whole string

course = "DCU \"Students\""     # Escape sequence - \ just saves the " character
name = "Roman \nPryima"         # Escape sequence - \n creates a new line
print(name)

first = "Roman"
last = "Pryima"

full_name = f"{first} {last}"
# f-string - is used to combine variables and text and also anything can be put inside of it
full_name = f"{len(first)} {25 + 15}"
print(full_name)

course = "Python for Beginners  "
print(course.upper())  # string method - makes all letters uppercase
print(course.lower())  # string method - makes all letters lowercase
print(course.title())  # string method - makes first letter of each word uppercase
# string method - removes whitespace from the left side or the right side of the from both if strip()
print(course.lstrip())
print(course.find("for"))  # finds the index of desired string
# replaces the first string with the second string
print(course.replace("Py", "IDK"))
# checks if the string is present in the variable and returns boolean value
print("for" in course)
# checks if the string is not present in the variable and returns boolean value
print("Beg" not in course)

# numbers

print(10*10 + 10/2)      # arithmetic operations
print(10 % 3)  # divides two numbers but prints only the remainder
print(10 // 3)  # divides two numbers but prints only the whole number
print(2 ** 3)  # exponentiation - raises number to the power of another number

x = 10
x = x + 3
x = 2 + 3j  # complex number

x = 10
x = x + 3
x += 3      # augmented assignment operator - adds 3 to the value of x
print(x)

print(round(-10.5))  # rounds the number
print(abs(-10.5))    # absolute value - makes the number positive
print(pow(3, 2))     # raises the number to the power of another number
print(max(3, 12, 5, 7))  # returns the maximum number
print(min(3, 12, 5, 7))  # returns the minimum number
print(int(10.5))     # converts float to integer
print(float(10))     # converts integer to float
print(complex(2, 3))  # creates a complex number
print(complex(2))     # creates a complex number with 0 imaginary part

print(math.ceil(2.3))

x = input("x: ")   # input function - takes input from user
# print(type(x)) # checks the type of variable
y = int(x) + 1  # converts the input string to integer

int(x)  # converts string to integer
float(x)  # converts string to float
bool(x)  # converts string to boolean
str(x)  # converts integer to string
# 0 is False, any other number is True, empty string is False, any other string is True, None is False.
print(bool(0))
print(bool(234))
print(f"x: {x} y:  {y}")
