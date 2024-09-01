# #question 1) Addition of two nums

# val1 = int(input("enter first number: "))
# val2 = int(input("enter second number: "))

# #if i hadn't typecasted the values, then the output would have concatenated both the values since the input is always a string in python
# print( "The sum of two  numbers is",val1 + val2)

# #question 2) Calculate area of square

# side = float(input("enter side: "))
# print("area is: ", side*side )

# #question 3) Average of floating point numbers

# a = float(input("enter 1st num: "))
# b = float(input("enter 2nd num: "))
# print("average is: ", (a+b)/2)

# #question 4) relational opeartor

# a = int(input("enter 1st num: "))
# b = int(input("enter 2nd num: "))
# print(a>=b)

# #q5) input name, and print length

# name = input("what is your name: ")
# print(len(name))

# #q6) occurrence of a letter in a string.

# string = "my name is laiba"
# ch = input("enter the character: ")
# print(string.count(ch)) #num of times ch occurred
# print(string.find(ch)) #first index at which it was found

# #q7) check odd or even.

# num = int(input("enter number: "))
# if(num%2 == 0):
#     print("even")
# else:
#     print("Odd")

# #q8) find max number:

# num1 = int(input("enter 1st number: "))
# num2 = int(input("enter 2nd number: "))
# num3 = int(input("enter 3rd number: "))

# if(num1>=num2 and num1>=num3):
#     print("Highest is number ", num1)
# elif(num2>=num1 and num2>=num3):
#     print("Highest is number ", num2)
# else:
#     print("Highest is number ", num3)


# #q9) multiple of 7 or not

# num = int(input("enter a number: "))
# if(num%7 == 0):
#     print(num, "is a multiple of 7")
# else:
#     print(num,"is not a multiple.")


# #q10) enter 3 movie name and store them in a list

# movies = []
# m1 = input("enter 1st movie: ")
# m2 = input("enter 2nd movie: ")
# m3 = input("enter 3rd movie: ")
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)


# #q11) palindrome checker

# list1 = [1, 2, 3, 2, 1]

# copy_list_1 = list1.copy()
# copy_list_1.reverse()

# if(list1 == copy_list_1) :
#     print("It is a palindrome")
# else :
#     print("not a palindrome")

# list2 = ["laiba", "zafir"]

# copy_list_2 = list2.copy()
# copy_list_2.reverse()

# if(list2 == copy_list_2) :
#     print("It is a palindrome")
# else :
#     print("not a palindrome")


# #q12)count the number oF students with grade A

# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"), "students got A")

# my_list = list(tup)
# my_list.sort()
# print(my_list)



# #q13) storing keys in dictionary

# dictionary = {
#     "table" : ["a piece of furnitrue", "list of facts and figures"],
#     "cat" : "a small animal."
# }

# print(dictionary)


# #q14) You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++" ,"C"}
# print(len(subjects), "classrooms are needed")



# #q15) WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# subject = {}
# marks1 = int(input("Enter marks for subject Math: "))
# marks2 = int(input("Enter marks for subject Comp: "))
# marks3 = int(input("Enter marks for subject Science: "))

# subject.update({"Math" : marks1})
# subject.update({"Comp" : marks2})
# subject.update({"Science" : marks3})

# print(subject)



# #q16)Figure out a way to store 9 & 9.0 as separate values in the set.

# collection = {("int", 9), ("float", 9.0)}
# print(collection)



# #q17) print elements using loops

# collection = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# #using while loop
# i = 0
# while i < len(collection) :
#     print(collection[i])
#     i+=1

# #using for loop
# for var in collection :
#     print(var)

# #q18) search for a number x usinf loops

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("enter the number you want to find: "))

# #using while loop
# i = 0
# while i < len(tup) :
#     if( x == tup[i]) :
#         print("number found at index ", i)
#     i+=1

# #using for loop
# for var in tup :
#     if( var == x) :
#         print("number found")
#         break
# else :
#     print("not found")


# #using FOR loop and RANGE()
# #q19)print num 1 to 100

# for i in range(1, 101) :
#     print(i)

# #q20) print num 100 to 1

# for i in range(100, 0, -1) :
#     print(i)

# #q21) multiplication table of n

# x = int(input("enter number: "))
# for i in range(1, 11) :
#     print(i * x)

# #q22)sum of first n numbers using while

# n = int(input("enter number: "))
# i = 1
# sum = 0
# while i <= n :
#     sum+=i
#     i+=1
# print("sum : ", sum)

# #q23) factorial of n number
# n = int(input("enter number: "))
# factorial = 1
# for i in range(1, n+1) :
#     factorial*= i
#     i+=1
# print("Factorial : ", factorial)


# #q24) function to print length of list

# def print_list(val) :
#     return len(val)

# num = [1, 2, 3, 4, 5]
# print(print_list(num))

# #q25) function to print elements of list

# def print_elements(list) :
#     print(list)

# val = ["laiba", "tulips"]
# print_elements(val)

# #q26) factorial of n

# def cal_fact(n) :
#     fact = 1
#     for i in range(1, n+1) :
#         fact *= i
#         i+=1
#     return fact

# factiorial = cal_fact(4)
# print(factiorial)


# #q27) function to convert USD -> PKR

# def USD_to_PKR(dollar) :
#     return (dollar * 278.6)

# rps = USD_to_PKR(3)
# print(rps)

# #q28) function to tell number odd or even

# def odd_even_checker(num) :
#     if(num%2 == 0) :
#         print("even")
#     else :
#         print("odd")

# odd_even_checker(8)
# odd_even_checker(90)
# odd_even_checker(7)
# odd_even_checker(79)

# #q28) recursive function to add first n numbers

# def add(n) :
#     if(n == 0) :
#         return 0
#     else:
#         return n + add(n-1)
    
# print(add(10))
# print(add(0))
# print(add(1))
# print(add(5))

# #q28) recursive function to print list elements

# def display(elements, index) :
#     if index == -1 :
#         return
#     else:
#         display(elements, index-1)
#         print (elements[index])
         

# val = [1, 2, 3, 4]
# length = len(val) -1

# display(val, length)

#q29) create a file nd add data in it

with open("practice.txt", "w+") as f:
    f.write("Hi everyone\nI am learning file Input/Output\nusing java\n")
    f.write("I like using java")

def replace_() :
    with open("practice.txt", "r+") as f:
        content = f.read()
        new_content = content.replace("java", "python")
        f.seek(0)
        f.write(new_content)

with open("practice.txt", "r") as f:
    content = f.read()
    if "learning" in content : #can use find function
        print("exists")

replace_()

