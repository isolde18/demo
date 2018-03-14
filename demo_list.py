#lists can be thought of as a series of boxes;
#each box having different value assigned;
#append is used to add a new item to the end of the list;
#len returns how many items are in a list;
#the valid indexes (as in numbers that can be used inside of the [])of a list
#range from 0 to len-1);the index function tells where the first location of
#an item is located in a list;
#to get help on all the functions, type help(list) in the interactive Python interpreter;

demolist=["life",42,"the universe",6,"and",9]
print ("demolist=",demolist)
demolist.append ("everything")
print ("after 'everything' was appended demolist is now:")
print (demolist)
print ("len (demolist)=",len(demolist))
print ("demolist.index(42)=",demolist.index (42))
print("demolist [1]=",demolist[1])

#Next loop through the list

for c in range (len(demolist)):
    print ("demolist[",c,"]=",demolist[c])#creates a variable c,which starts at 0

del demolist[2]
print ("After the 'universe' was removed demolist is now:")
print(demolist)
if "life"in demolist:
    print("'life' was found in demolist")
else:
    print("'life'was not found in demolist")
if "amoeba" in demolist:
    print ("'amoeba' was found in demolist")
if "amoeba" not in demolist:
    print("'amoeba' was not found in demolist")
another_list=[42,7,0,123]
another_list.sort()
print ("The sorted another_list is", another_list)
