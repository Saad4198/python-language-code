"""
IN THIS WE LEARN WHO TO LIST METHOD ARE PERFORM ON LIST JUST LIKE STRING AND WE USED SOME LIST METHOD AND ONE IMPORTANT THING WHEN WE USED LIST SO WE USED THESE TYPE OF BRACKET [] AND AND WE USED ALSO THIS TYPE OF BRACKET {} SO ONE PROBLEM OCCUR WHEN WE GIVE VARIABLE VALUE ANS NOT GIVE SAME JUST LIKE THEY WANT AND GIVE VALUE TO THE VARIABLE,and check both variable output value BY USING BOTH BRACKET. 
"""
friends=["Saad","ALI", "FAHAD","TAYYAB",15.2 ,"SAFIAN"]
print(friends)
friend1={"ALi","Ahmed","Saad",444,76767.77,"Fahad","Tayyab"}
 #we are not used these braces in lists{} because it will not give me correct ans.
print(friend1)
#lists methods apply
#appends means add data in the list at the end of the lists.
print(" 1. APPEND METHOD APPLy")
friends.append("SARGODHA")
print(friends)
#friend1.append("Lahore") #in the variable append are not apply because we used these {} braces
#print(friend1)
print("2. UNSORTED DATA CONVERT IT INTO SORTED DATA")
l1=[1,4,5,7,4,2,5,9,66,88,34,22]
print(l1) #if we unsort data convert it into sorted so we used these 
l1.sort()
print(l1)
print("3. CONVERT THE DATA INTO REVERSE ORDER")
l2=[22,4,3,2,3,4,5,77,88,44,66,88,55]
print(l2) #IF WE PRINT LIST IN REVERSE ORDER SO WE USED THESE
l2.reverse()
print(l2)
print("4.ADD THE DATA AT THE SPECIFC POSITION")
l3=[22,24,26,27,28,29,30,31,32,33]
print(l3)
l3.insert(1,23) #if we add data at specific position first index number and then value add 
print(l3)
print("5. if we delete any data so we used pop")
l4=[1,2,3,4,5,6,7,29,22,34,56,78,89,90]
#l4.pop(7)
#print(l4) they are not return value means value are not show
print(l4)
print("the value are delete",l4.pop(7)) #they are used for return value we used this because these are return value
print(l4)
print("6. specific vaulue delete form the list")
l5=[22,24,25,89,30,34,35,37,39,40]
print(l5)
l5.remove(89) #we remove the value are 89 
print(l5) #print the value after delete
       