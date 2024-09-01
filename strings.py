#concatenating two strings

str1 = "my name is"
str2 = "Laiba"
print(str1 + " "+ str2)

#length of string

print(len(str1))
print(len(str2))
print(len(str1 + str2))

#indexing
#+ve index, -ve index.
#+ve index is like moving forward in the string(1, 2, 3,...), and -ve index is like moving backwards in the string(...-3, -2, -1)
#if you move forward in the str2 then LAIBA +ve index would be ([0]=L, [1]=A...). Whereas, moving ackwards neagtive looks like([-1]=A, [-2]=B).

print(str1[3]) #access the third index element, but can not manipulate it.
# str1[0] = "e"  this gives error
print(str2[-2])

#slicing
#-ve indexes are mostly for slicing.
#slices part of the string.

print(str1[1: 9]) #the last index is skipped
print(str1[3 : 7] + " " + str2[0 : 6])

#if one want to go to the last index
print(str1[3: len(str1)]) 
#or
print(str1[3: ]) #[3 : 10]
print(str1[ : 5]) #[0: 5]

#-ve slicing
print(str1[-6 : -10]) 

#some strings function

print(str1.endswith("is"))
print(str1.capitalize()) #capitializes the first index character
print(str2.replace("Laiba", "bilal"))
