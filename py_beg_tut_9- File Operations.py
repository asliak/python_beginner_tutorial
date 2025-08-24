file = open("myfile.txt","r")
file.close()

with open("file.txt","r") as f:
    content = f.read()

print(content)

file = open("file.txt","r"):
content = file.read()

file.close()
print(content)

file = open("file.txt","w")
file.write("Hello Youtube")
file.close()
file.flush() # to save the data

from os import *
mkdir("test") # make directory
chdir("test") # change directory
mkdir("newdir")
rename("file.txt", "myfile.txt") # rename file
remove("myfile.txt") # remove file