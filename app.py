import addition as a
import subtraction as s
import multiplication as m
import division as d


print("Welcome to the simple calculator, please select the operation to perform:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Divide two numbers")

user_input = input()
user_input = int(user_input)


if user_input == 1:
    num1 = input("Enter first number:")
    num1 = float(num1)
    num2 = input("Enter second number:")
    num2 = float(num2)
    result = a.add_two_numbers(num1, num2)
    print(result)

elif user_input == 2:
    num1 = input("Enter first number:")
    num1 = float(num1)
    num2 = input("Enter second number:")
    num2 = float(num2)
    result = s.subract_two_numbers(num1, num2)
    print(result)

elif user_input == 3:
    num1 = input("Enter first number:")
    num1 = float(num1)
    num2 = input("Enter second number:")
    num2 = float(num2)
    result = m.multiply_two_numbers(num1, num2)
    print(result)

elif user_input == 4:
    num1 = input("Enter first number:")
    num1 = float(num1)
    num2 = input("Enter second number:")
    num2 = float(num2)
    result = d.divide_two_numbers(num1, num2)
    print(result)

else:
    print("Invalid entry")
