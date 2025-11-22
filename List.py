
#Lists are the builtin datatypes which stores all types of data, which are seprated by commma
#List are mutable which means which can be changes and immutable means which cannot be changed i.e strings

marks=[20,19,17,20,26]
print(type(marks))
print(len(marks))

#the list are mutubable means which can be changed.
marks[0]=15  
print(marks)

#list can also be indexed and sliced
print(marks[0:len(marks)])
print(marks[:4])

#The list can also be in negative number slicing
negative=[1,2,3,4,5]
        #[-5,-4,-3,-2,-1]


#list methods

#1)list.append() add the element to the last of list
negative.append(100)
print(negative)

#2)list.sort() sorts the elements in ascending order
negative.sort()
print(negative)

#3)list.sort() sorts the element in descending order.
negative.sort(reverse=True)
print(negative)


#5)list.insert(idx,element) #insert element at index
negative.insert(0,777)
print(negative)

#4)list.reverse() reverse the list
negative.reverse()
print(negative)


#Wap to ask the user to enter their 3 favourite movies names and stores them in list

movies=[]

movie1=input("Enter the movie1:")
movie2=input("Enter the movie2:")
movie3=input("Enter the movie3:")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)
print(len(movies))

#Wap to check if the list conatins palindome elements.
list=[1,2,1]
print(list)
list_copy=list.copy()
list_copy.reverse()
print(list_copy)

if (list==list_copy):
    print("list is palindrome")
else:
    print("List is not palindome")

#Wap to store the values in list and sort them From A to D 

grade=[]

for i in range(1,8):
    var=input("enter the values:")
    grade.append(var)
print(grade)    

grade.sort()
print(grade)