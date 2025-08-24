mylist = [10, 20, 30, "string", True, 8.97]
print(mylist)
print(mylist[3])
print(mylist[:3])
print(mylist[1:3]) # element at index 3 is excluded
print(mylist[-2]) # second last element

mylist[3] = "another string"
print(mylist)

for x in mylist:
    print(x)

mylist = [1, 2, 3, 4, 5]

for x in mylist:
    print(2 ** x)

x = [1, 2, 3]
y = [4, 5, 6]

print(x + y) # concatenation

x = [1, 2, 3]
y = [4, 5, 6, "hello", True]

print(x * 4) # repetition

print(len(x)) # length of list
print(max(x)) # maximum element
print(min(x)) # minimum element

x.append("new value")
print(x)

x.insert(2, "another value")
y.remove("hello")
x.pop(2)

y.pop(y.index("hello"))

a = [55, 6, 1 , 99, 2,  3]
a.sort()
print(a)
print(sorted(a)) 

x = [1, 2, 3]
y = (1, 2, 3) # its a tuple it cannot be modified
print(y[2])
# y[2] = 10 this will give an error

x = (1, 2, 3)
x = list(x) # converting tuple to list
x[2] = 10
x = tuple(x) # converting list back to tuple
print(x)

person = {'name': 'Mark', 'age': 25, 'gender': 'male'}
print(person)
print(person["age"])
person["new_key"] = "new_value"
print(person.items())
print(person.keys())
print(person.values())

x = [1, 2, 3]

print(2 in x)
print(7 in x)

print(2 not in x) 
print(7 not in x)

x = "hello" 
if type(x) is int:
    print("x is int")
else:
    print("x is not int")