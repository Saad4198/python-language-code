#write a program to find out whether a given post is talking about “any person” or not.
#ONLY ONE SPECIFIC PERSON
""" we used .lower() in if statement because they convert the value if they given in capitialized form so they convert it into lower alphabet if we not used these so give value so they are not match and give ans of else condition just like we give value SAAD so condition are not match with if statement so else condition run and if wee used lower() so the value of capitailzed convert it into lower alphabet """
print("FIRST PROGRAM")
post=input("ENTER THE POST:")
if("saad" in post.lower()):
    print("The posot is talking about saad")
else:
    print("The posot is not talking about saad")
print("\n Second program")
post=input("ENTER THE POST:")
if("saad" in post.lower()):
    print("The post is talking about saad")
elif("shamir" in post.lower()):
    print("The post is talking about shamir")
elif("fahad" in post.lower()):
    print("The post is talking about fahad")
elif("tayyab" in post.lower()):
    print("The post is talking about tayyab")
elif("safian" in post.lower()):
    print("The post is talking about safian")
elif("ali" in post.lower()):
    print("The post is talking about ali")
else:
    print("The post is not talking about anyone")