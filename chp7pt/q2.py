#Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
# it print only greet only cpaitilized alphabet S 
l=["saad","Fahad","Tayyab","Talha","Safian","Suleman","shamir","ali","abdul","taha","hamza"] #take value of list
for n in l:
    if(n.startswith("S")): #condition
        print(f"HELLO {n}") #result print
        
#if we both letter used so wee used these method
j=["saad","Fahad","Tayyab","Talha","Safian","Suleman","shamir","ali","abdul","taha","hamza"]
for i in j:
    if(i.startswith("S")) or (i.startswith("s")):
        print(f"HELLO {i}")  