hislist = ["apple", "banana", "cherry"]

for x in hislist:
    print( x );

if "apple" in  hislist:
    hislist.append("nova fruta")
    print( "Yes sim en lista" );

#Print the number of items in the list:
print( len(hislist) )

#Using the append() method to append an item:
hislist.append("nova fruta");

#Insert an item as the second position:
hislist.insert(1, "orange")
print(hislist)

#The pop() method removes the specified index, (or the last item if index is not specified):
hislist.pop()
print(hislist)

#The remove() method removes the specified item:
hislist.remove("cherry")
print(hislist)

#The pop() method removes the specified index, (or the last item if index is not specified):
hislist.pop()
print(hislist)

#The del keyword removes the specified index:
del hislist[1];
print(hislist)

#The del keyword can also delete the list completely:
del hislist
print(hislist)