hislist = ["apple", "banana", "cherry"]

for x in hislist:
    print( x );

if "apple" in  hislist:
    hislist.append("nova fruta")
    print( "Yes sim en lista" );


print( len(hislist) )

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
del hislist[3];
print(hislist)

#The del keyword can also delete the list completely:
del hislist
print(hislist)