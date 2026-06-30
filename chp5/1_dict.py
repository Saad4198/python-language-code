"""
In this file we learn python Dictionary how and why we used, and the syntax and why and how we write the syntax and code in dictionary.
"""
#Indictionary when we take build in value used 
#in dictonary are depend on two partion keys and values and it is also called KEYVALUE pair.
#IN this saad,lahore ,islamabad ,list and 0 are keys 
#in this 100,24536 ,23232,14081947 etc are the key value
name = {
 "Saad":100,
 "lahore":24563,
 "islamabad" :23232,
 "pakistan":14081947,
 "list":[1,2,3,232,2324,13134,67567],
  0:"saad"
}
d={} #this is empty dictionary
print("the empty dict",d) #print the empty dictionary
print(name) #it print the value if name.
print(type(name)) #it tells we used dictionary datatype used.
print("it print the marks of saad",name["Saad"])
print("it print the area of lahore",name["lahore"])
print("the value of list",name["list"]) #print the value of list
#in dictionary when we used user defined vlue take.
"""
this is the formula when we take user value take.
dictionary_name["Key"] = input("Enter value: ")  #formula
dictionary name means variable name and input value are have.
"""  
print("\n This after we take user defined value take")
student={}  #this is used for userdefined in value take so we used.
student["Name"] = input("Enter your Name:")
student["city"] = input("Enter your city:")
student["Department"] = input("Enter your Department:")
student["rollno"] = input("Enter your rollno:")
print(student)
information={}
information["Address"]= input("Enter you adress:")
information["job"]=input("enter your current working:")
information["degree"]=input("enter your degree:")
print(information)
