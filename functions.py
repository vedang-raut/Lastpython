
#wap to find a factorial of a number.(n is the parameter)


def fact(n):    
    count=1
    factorial=1
    while count<=n:
        factorial=factorial*count
        count+=1
    print(f"The factorial of a number {n} is:{factorial}")
    return factorial

fact(3)
    

n=int(input("Enter the number to find the factorial of:"))