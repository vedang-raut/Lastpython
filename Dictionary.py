
#Nested Dictionary
student={
    "Name":"Alex",
    "Subject":{
        "Science":20,
        "Maths":20
    },
    "Place":"Bombay"
 
}

#print(type(student))
#print(student["Subject"]["Maths"])


#Methods
print(student.keys()) #return all the keys
print(student.values()) #return all the values
print(student.items())  # return all the data in form of type of tuples
print(student.get("Place"))
print(student["Place"])

#dictionary.update() is a method where you can pass a new dict or a key value value pair
student.update({"car":"Jdm"})
print(student)

newdic={
    "Country":"Japan",
    "Culture":"Drift"
}
student.update(newdic)
print(student)
print(list(student))