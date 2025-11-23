#Sets are the builtin datatype which is used ti store the unorder set of element means they cannot be accessed with index.
#sets are mutuable datatype but element in sets are immutable.

sets={20,10,25,30,40}
print(type(sets))
print(len(sets))
print(sets)
#sets removes all the duplicates
remove_duplicates={1,2,3,3,3,5}
print(remove_duplicates)  #{1, 2, 3, 5} output is given is by removing the duplicates


#sets can also be created 
whoop={}
print(type(whoop))
whooping=set(whoop)
print(type(whooping))
whooping.add("Gtr")
whooping.add("jdm")
print(whooping)
whooping.remove("Gtr")
print(whooping)
whooping.add("mazda")
whooping.add("corvette")
whooping.pop()
print(whooping)
whooping.clear()
print(whooping)

#This are the special methods for the union and the intersection.
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1.intersection(set2))



#wap to store 9 and 9.0 in the set.
value1=int(input("Enter the no 9="))
value2=float(input("Enter the no 9.0="))
store={("int",value1),("flat",value2)}
print(type(store))
print(store)