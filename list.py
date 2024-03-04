 
mylist=[]
print(mylist)


mylist.append("10")
mylist.append("20")
mylist.append("30")
mylist.append("40")

print("update list = \n" ,mylist)


mylist.insert(1,"15")

print("update list = \n", mylist)


mylist.extend([50])
mylist.extend([60])
mylist.extend([70])

mylist.remove(70)

print("update list = \n",mylist)


print("sort list in ascending order")

print("update list = \n",mylist)

index_value = mylist.index(30)

print(f"{30} is not in the list.")