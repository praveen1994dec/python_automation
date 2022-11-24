file = open("test.py")
print(file.read())

#Create a File:

file = open("Text2.txt", "x")



#write to a file

file = open("Text.txt", "w")
file.write("This is an example of file creation.")
file.close

#Read a File:

file = open("Text.txt", "r")
print(file.read())
file.close

#Append a File:

file = open("newText.txt", "a")
file.write("This is an example of file appending.")
file.close