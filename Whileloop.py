
#Wap to search a X number in the list
search=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=int(input("Enter the number from list:"))
count=0
idx=0
while count<=9:
    case=search[idx]
    if (case==x):
        print(f"The number {x}is found at index{idx}")
        break
    else:
        print("Not found")
    idx=idx+1
    count=count+1