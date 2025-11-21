
#wap to enter marks of 3 subjeects from the user and store them in a dictonary.

students={}
marks1=int(input("Enter the marks:"))
marks2=int(input("Enter the marks:"))
marks3=int(input("Enter the marks:"))
students.update({"English":marks1})
students.update({"Maths":marks2})
students.update({"Chemistry":marks3})
print(students)