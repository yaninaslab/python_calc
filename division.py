
def divide_two_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print("Can't divide by zero!")
    except:
        print("Sorry, something went wrong!")
