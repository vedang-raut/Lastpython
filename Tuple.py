#the tuple is built in datatype which is immutable means which cannot be changed.
#It is given by round bracket and seprated by commas.

#Note that tuple can only be initalised if only the particular element is given comma
tup=(1)
print(type(tup))

tuple=(1,)
print(type(tuple))  #Here the comma is given

num=(2,3,4,5,8,2)
print(num[0:2])

#methods in tuple
print(num.count(2))
print(num.index(2)) #at what index the 2 is 


tuple=('A', 'A', 'A', 'D', 'F', 'S', 'S')
print(tuple.count('A'))