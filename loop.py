#while loop is usually used when travelling index by index
#finding a number in a list/tuple is called linear search(single line search) 

count = 1
while count <=100 :
    print(count)
    count += 1 


i = 100
while i >=1 :
    print(i)
    i -= 1 

n = int(input("enter number: "))
i = 1
while i <= n :
    print(n, "x", i, "=", n*i)
    i+=1


numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(numbers) :
    print(numbers[i])
    i+=1

numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("enter number you want to find: "))
i = 0
while i < len(numbers) :
    if(x == numbers[i]) :
        print("num found at index", i)
    i+=1

#for loop is usually when we travel sequentially

lists = [1, 2, 3, "laiba", "zafir "]

for val in lists : #this copies the list elements into newly created var one by one.
    print(val)

    
string = "my name is laiba"
for char in string :
    print(char)
else : #usually used with break
    print("an optional else...end")


for char in string :
    if(char == "l"):
        print("found!")
        break
else : 
    print("not found")

#RANGE FUNCTION : starts from 0 and increemnts 1 by default.
#range(start, stop, step) or range(start, stop) or range(stop)

print(range(10))
seq = range(10)
print(seq[4])
#or
for i in seq :
    print(i)
#OR
for i in range(10): #range(stop)
    print(i)

for i in range(3, 9) : #range(start, stop)
    print(i)

for i in range(5, 50, 4) : #range(start, stop, step)
    print(i)



