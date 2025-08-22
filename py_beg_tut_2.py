print("Hello, World!")

# str "hello" or can be 'hello'

# ''' triple quotation marks for multi_line strings'''

# int 10 9 -3
# float 10.9 9.345 -8.763
# complex(10, 5) -> 10 + 5j

# bool True False

# list [1, 2, 3, 4] or ["apple", "banana", "cherry"]
# tuple (1, 2, 3) or ("apple", "banana", "cherry")
# set {1, 2, 3} or {"apple", "banana", "cherry"}
# dict {"name": "John", "age": 30}

print("10"+ "10") # adds up both strings together, not the numbers
print(10 + 10) # normal math addition

print(type(10)) 
print(type("10"))

x = 10
y = 20
whatever = True

print(x)
print(x + y)

# python is a dynamically typed language
# you don't need to declare the type of variable
# it figures it out on its own
# you can change the type of variable
x = 10
x = "hello"
x = True

## typecasting
x = "120"
x = int(x)
print(x / 4)