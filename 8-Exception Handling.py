try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    print(x / y)
except:
    print("There was an error!")

try:
    x = int(input("First number: "))
    y = int(input("Second number: "))
    print(x / y)
except ValueError::
    print("Please enter a valid number next time!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
    y = 1 
    print(x / y)
finally:
    print("DONE")

def some_function():
    if condition:
        raise ValueError("Something went terribly wrong!")

some_function()

x = 10
y = 20

assert(x < y)
