
#Wap to store the values in list and sort them From A to D 

grade=[]

for i in range(1,8):
    var=input("enter the values:")
    grade.append(var)
print(grade)    

grade.sort()
print(grade)