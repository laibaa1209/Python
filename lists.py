numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[3])

#in lists we can store umsimilar data type elements.
values = ["laiba", 18, "FAST", 49.5]
print(values)
print(type(values))
print(len(values))
print(values[3])

#likewise string, slicing is also incoperated in lists. (ending index not included)

print(numbers[3:7])
print(values[:len(values)])

#some of lists function
#any changes in the lists is called mutation.

val = [4, 8, 2, 10, 9, 5]
val.sort() #sorts the elements in ascending order
print(val)

val.append(11) #add value to the last
print(val)

val.sort(reverse = True) #sorts the elements in descending order
print(val)

val2 = ["laiba", "fatima", "aira"]
val2.reverse() #reverses the list
print(val2)

val2.insert(1, "zafir")
print(val2) #insert element at a certain index

val2.remove("laiba")
print(val2) #removes the values

val2.pop(2) #removes value at the given index
print(val2)