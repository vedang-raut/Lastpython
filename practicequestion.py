
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