
#take the input from the user and sum of the number
a=int(input("The first number:"))
b=float(input("The second number is:"))
sum = a + b
print(f"The output given is {sum}")

#Wap to input users first name and print its length.

name=input("Enter the initial name:")
length=len(name)
print(length)

#Wap to find the occurence of dollar
string=input("Enter the string :")
print(string.find("f"))

#wap for checking if the number is palindrome or not.
#string[start : end : step]
#start: not given → start from the end
#end: not given → go until the beginning
#step: -1 → move backwards one character at a time
string=input("Enter the string for checking:")
             
if string==string[::-1]:
    print("the string is palindrome")
else:
    print("The string is not palindrome")

#string[::1]:
#start → not given → means start from the beginning
#end → not given → means go till the end
#step = 1 → move forward one character at a time



#wap where you have list of subjects. Assume one classroom for each subject and how much classrooms are require.
Subjects=["python","java","c++","python","javascript","java","python","java","c++","c"]
classroom=set(Subjects)
print(len(classroom))

classroomcount=tuple(classroom)
print(classroomcount)
