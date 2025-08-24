def helloworld():
    print("Hello World!")

helloworld()

def add(x, y):
    print(x + y)

add(19, 12)

def add_return(x, y):
    return x + y    

result = add_return(19, 12)
print(result)

def mysum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(mysum(10, 20))

print(mysum(10, 20, 30, 40, 50))
