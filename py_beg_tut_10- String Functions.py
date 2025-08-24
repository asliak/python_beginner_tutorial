text = "Hello World!"
print(len(text))
print(text[2])

for letter in text:
    print(letter)

print(text[6:])

text2 = "Hello World!\nThis day is awesome!"
print(text2)

name = input()
age = int(input())
print("My name is " + name + " and I am " + age + " years old.")
# OR
print("My name is %s and I am %d years old." % (name, age))
# OR
print("My name is {} and I am {} years old.".format(name, age))

text3 = "This is my text!"
text3 = text3.upper()
print(text3)
text3 = text3.lower()
print(text3)
text3 = text3.title()
print(text3)
text3 = text3.swapcase()
print(text3)

text4 = "I am Mike and my life is beautiful! Because of my job!"
print(text4.count("my"))
print(text4.count("i") + text4.count("I"))

text5 = "I am Mike and I feel great!"
print(text5.find("Mike"))

seperator = ";"
mylist = ["Kitchen", "Dog", "Mike"]
seperator.join(mylist)

text6 = "I am happy because my name is Mike!"

words = text6.split(" ")
print(words)

text7 = "I am Mike! My name is Mike!"
print(text7.replace("Mike", "Sara"))