marks = int(input("enter your marks: "))

if(marks>=90) :
    grade = "A"
elif(marks>=80) :
    grade = "B"
elif(marks>=70) :
    grade = "C"
else :
    grade = "fail"

print("The Grade of student is: ", grade)