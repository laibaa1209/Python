file = open("laiba.txt", "r")
data = file.read() #50 indicates the number of places till the data to be printed. and () means all the data
print(data)
print(type(data))

#you can also read the data line by line 
line1 = file.readline()  #after reading the data from file once, the cursor moves towards the end of line, so when i will try to print the data in the new line, the new line will be emtpty since the cursor is pintinf to the last line, therefore the output will be -> empty space
print(line1) #reads one line and move to the next line

line2 = file.readline() #reads the next line move to the next line to itself...and so on..
print(line2) 
file.close()

# -------------------------WRITING TO A FILE-------------------------

file = open("laiba.txt", "w")
file.write("i am learning python") #overwrites the already present data
file = open("laiba.txt", "r")
data = file.read()
print(data)

file = open("laiba.txt", "a")
file.write("\tpython is pretty easy") #appends to the already present data
file = open("laiba.txt", "r")
data = file.read()
print(data)
file.close

# creates a new file, if one doesn't exist by the speicifed name, if open in append or write mode
f = open("python.txt", "w")
f.write("pythonnnn")
f.close()

f = open("python.txt", "r")
data = f.read()
print(data)
f.close()

#r+ mode points the cursor to the begning of the file (r+ = read and write data)
f = open("python.txt", "r+") #in r+ you can overwite to the file but it doesn't truncatet it and read it, in w+ you can read from the file and it over writes and truncates(points at the start)
f.write("laib")
data = f.read()
print(data) #output -> onnnn, because i appended laib and the cursor is pointing to its next location, which is o.
f.close() #if you want the whole output then open it in read mode again.

#with syntax automatically closes the file.
with open("my.txt", "r+") as file_name :
    file_name.write("my name is laiba")
    file_name.seek(0) #take the pointer back to 0th position
    content = file_name.read()
    print(content)

# -------------------------DELETING A FILE-------------------------
#you can use module for this. 
import os #os is a module

os.remove("my.txt") #delets the file
