myTechlist = ["python","database","azure","reactjs"]
myTechlist2 = ["Aws",]
# Appending html to myTechlist
myTechlist.append("html")


# print item on index 2
print (myTechlist[2])


# print the lenght of your list
print(len(myTechlist))

# insert AWS, Cybersecurity
myTechlist.insert(5,"Cybersecurity")

# extend myTechlist to myTechlist2

myTechlist.extend(myTechlist2)

# use remove method
myTechlist.remove("html")

# use pop method
myTechlist.pop(1)

# use delete method
del myTechlist[2]
print(myTechlist)