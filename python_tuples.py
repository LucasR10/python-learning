thistuple = ("apple", "banana", "cherry")
print(thistuple)

#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#You can loop through the tuple items by using a for loop.
for x in thistuple:
  print(x)

#Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#uma vez uma tuple e criada, voce nao pode add items para ela. Tuples sao nao modificavel.
#You cannot add items to a tuple:

#thistuple[3] = "orange" # This will raise an error
print(thistuple)

#The del keyword can delete the tuple completely:
del thistuple
#  print(thistuple) - > esto vai causar um error por que o tuple nao mais existe

#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.

#Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets is a constructor
print(thistuple)


#Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
print(thistuple.count)
# index()	Searches the tuple for a specified value and returns the position of where it was found
print(thistuple.index)

"""
   SET A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
"""


thisset = {"apple", "banana", "cherry"}
print(thisset)

#Loop through the set, and print the values:
for x in thisset:
  print(x)

#Check if "banana" is present in the set:
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset.update(["orange", "mango", "grapes"])
thisset.add("orange")

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)

x = thisset.pop()

"""
add() - Adds an element to the set
clear() - Removes all the elements from the set
copy()  -  Returns a copy of the set
difference() - Returns a set containing the difference between two or more sets
difference_update()  - 	Removes the items in this set that are also included in another, specified set
discard() - Remove the specified item
intersection()  - 	Returns a set, that is the intersection of two other sets
intersection_update()	 - Removes the items in this set that are not present in other, specified set(s)
isdisjoint() - Returns whether two sets have a intersection or not
issubset() - Returns whether another set contains this set or not
issuperset()  - Returns whether this set contains another set or not
pop() - Removes an element from the set
remove()  - Removes the specified element
symmetric_difference()  - 	Returns a set with the symmetric differences of two sets
symmetric_difference_update()  - 	inserts the symmetric differences from this set and another
union()	 - Return a set containing the union of sets
update() - Update the set with the union of this set and others
"""