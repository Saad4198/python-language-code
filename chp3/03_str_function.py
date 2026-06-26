#in this file we learn string function detail
#1.This function represent the length of the name value.
name="MSAAD"
print(len(name))
#1. if we check the name value with these name check if they same give yes otherwise false value.
#check end value
print(name.endswith("aad"))    #this is false because small alphabets are given in print
print(name.endswith("AAD"))    #this is true because big alphabets are given in print
print(name.startswith("MSA"))   #This is true because big and same alphabets are given in print
print(name.startswith("msa"))   #this is false because small alphabets are given in print.
print(name.startswith("MSD"))  #This is false because last alphabets are given in pront are different.
#2. if wee check the name in varaible value are repeat in the variable value they used to check.
print("\n 2nd string function count value are repreat")
name = "msaaad"
count = name.count("a") #these are used to check the word are repeatin the name value just like a is 3 time.they check.
print("A is repreat in these value" ,count) 
count=name.count("s") #these are used to check the word are repreat in the name value just like s is 1 time. they check.
print("S is repreat in these variable value", count)
count=name.count("h") #these are used to check the word are repreat in the name value just like his 0 time. they check.
print("h is repreat in the variable value", count)
# 3. if we variable value alphabets first letter are cpitalized so we used these commands
print("\n captilized name value first letter")
name="msaaaad"
print(name.capitalize())   #they only capitalized M because its first letter
name1="MSAaad"
print(name1.capitalize())   #if we give three or all valuw they only capitalized first leeter remain short.
# these are used to check they are have in vlaue and check the start index point print andnot found so give -1 value.
print("\n They are used to check the index value if have so give ans:")
name = "fahad"
index = name.find("ha")
print(index)
index=name.find("sa")   #if not found so ans is -1 just like second print ans is -1 and first print give correct ans
print(index)