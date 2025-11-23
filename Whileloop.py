

#Wap to get sum of first n natural numbers.
n=int(input("Enter the number:"))
count=0
sum=0
while count<=n:
    sum=sum+count
    print(f"{sum} is at round {count}")
    count=count+1
print(f"The final sum is {sum}")