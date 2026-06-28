"""
the pic are add for information it tells that the string are immutable and string data are not changed so we used list data to changed data if we changed and pic check if we changed string index 3 value are A convert it into H and it is not convert the data.
"""
#In programming language we used array but python collection of data are called list not array.
#becuse we are not change string data because it is immutable and it is not change the string value.
friends=["ALi","Ahmed","Saad",444,76767.77,"Fahad","Tayyab"]
print("The value are store in the list array are show:\n", friends) #this print all the list data
print("\n The index 6 value are tayyab and show data :",friends[6]) #this print only index 6 data before comma every data represesnt ine index just like ali start 0 index and so on.
friends[3]="lahore" #we changed the index 3 value 444 convert it into lahore and check it into output
print("\nThey convert index 3 value 444 convert into lahore:",friends[3])
#we used same list sciling just like same string scilicing of the array.
print(friends[1:5])
