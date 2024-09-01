#have no order(no indexes)
#unique and immutable elements (lists and dic cannot be stored in sets)
#sets aremutable but their elemnts are immutable


collect = {7, 8, 2, 3, "cpp", "python" }

print(type(collect))
print(len(collect)) #total number of items

#if you add duplicate elements in the set, it will ignore it

Set = {1, 2, 3, 2, 2, "laiba", "python"}
print(Set)

#for empty set
#collect = {} but this is an empty dictionary not empty set
collect = set() 
print(type(collect))
print(len(collect))

#methods of sets
Set = {1, 2, 3, 2, 2, "laiba", "python"}

Set.add("girllll")
print(Set)

Set.remove(2)
print(Set)

print(Set.pop()) #removes random value

#Set.clear()  #empties the whole set
#print(Set)

Set.add((10, 9, 1209))
print(Set)

#Set.add([78, 98]) # -> unhashable type(list cannot be an item of set)


#union and intersection methods work similar like mathematics
union_set = Set.union(collect)
print(union_set)

print(Set.intersection(collect))

