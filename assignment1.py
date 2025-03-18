# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter second number: "))

add = number_1 + number_2
sub = number_1 - number_2
mul = number_1 * number_2

print(f"The sum of {number_1} and {number_2} = {add}")
print(f"The difference between {number_1} and {number_2} = {sub}")
print(f"The product of {number_1} and {number_2} = {mul}")
