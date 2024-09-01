#can have nested dictionary
#key can be of type string, int, float or tuple since they are immutable
#key:value pair
#dictionary is mutable but it's keys are immutable
#they are unordered(have no indexes) and donot allow duplicate keys

student = {
    "key" : "value",
    "name" : "laiba",
    "age" : 19,
    "education" : "undergraduate student",
    "is_above_18" : True,
    "subjects" : ["PAI", "DS", "DSA"],
    "topics" : ("python", "C", "CPP"),
    "marks" : 98.9
}

print(type(student))
print(len(student))
print(student)

#print a single key
print(student["name"])
student["name"] = "zafir" #overwrites the old one
student["surname"] = "zia"

#a null dictionalry
null_dict = {}
print(null_dict)
null_dict["age"] = 19
print(null_dict)

#nested dictionary
semester = {
    "semester_name" : 2,
    "courses" : {
        1 : "MVC",
        2 : "DLD",
        3 : "OOP"
    },
    "marks" : {
        "MVC" : {
            "marks" : 94.8,
            "course code" : "MT107" 
        },
        "OOP" : {
            "marks" : 98.3,
            "course code" : "SS234" 
        },
        "DLD" : {
            "marks" : 86.3,
            "course code" : "EE987" 
        }
    } 
}

print(semester)
print(semester["courses"])
print(semester["courses"][1])
print(semester["marks"])
print(semester["marks"]["MVC"])
print(semester["marks"]["MVC"]["marks"])


print(student.keys()) #prints all the keys. (prints all the keys)
print(list(student.keys())) #type casted into list
print(student.values())
print(student.items()) #return values in tuple pairs
list1 = list(student.items()) #dict into list
print(list1[0]) #list first pair accesed which was in tupple form


#two ways to get value of keys
#1. method...2. manually
#second method
print(student["name"]) # if by accidentally i type the wrong key name -> error
#1st method
print(student.get("name")) # if by accidentally i type the wrong key name -> None

#it's better to use methods instead of line num 76 because in that case it throws error and stops the later rogram from executing, while the method returns none and executes the code after it safely 
print("before")
#print(student["name1"]) 
print(student.get("name1")) 
print("after")


#update dictionary 
student.update({"name" : "fatima"})
print(student)

new_student = { 
    "name" : "aira",
    "uni" : "FAST",
    "name1" : "Zafir"
}

student.update(new_student)
print(student)
 