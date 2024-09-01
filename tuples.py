#tuples are immutable like strings(cannot manipulate the data in them)

tup = ()
tup1 = (1,)
tup2 = (1, 2, 3, 2, 4,2)
print(type(tup1))
print(tup)
print(tup1)
print(tup2)

x = ("laiba", "zafir", 18, 9)
print(x)

#some tuple methods
print(tup2.count(2)) #occurrences of the same number
print(tup2.index(2)) #first occurrence index return

