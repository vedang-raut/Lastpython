
#wap to find the sum of the first n natural numbers.
n=int(input("Enter the last n  natural number: "))
sum=0
for i in range(0,n+1):
    sum=sum+i
    print(f"The sum of this round{i} is {sum}")

print(f"The final sum is: {sum}")