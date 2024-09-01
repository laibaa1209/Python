def display(n) :
    if (n == 0) :
        return 0
    display(n-1)
    print(n)
    

display(10)

def fact(n) :
    if(n == 0 or n == 1) :
        return 1
    else:
        return n* fact(n-1)
    
print(fact(5))