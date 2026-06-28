"""
In this we check who the method of tuple apply on data
"""
print("1. It tells count the data")
a=(23,34,45,24,5,4,23,45,65,32,54,64,42,23)
print(a)
no=a.count(23) #it tells how many type data or value are come in variable value
print("it count the value 23 repeat",no)
print("\n 2. It tells the index number of the data")
b=(34,45,233,344,24,13,"Sargodha","lahore","SAAD","FAHAD")
print(b) #value position number find
id=b.index("SAAD")
print("it tells the indexx number of value Saad::",id)
print("\n 3. It IS used to describe the length of the variable value length ")
print("the value of b is",b)
print("it tells the length of the varibale length b::",len(b)) #length describe how many length of the variable value
print("it tells the value of a is",a)
print("it tells the length of the varibale length a::", len(a))
print("\n 4. check the value are have:")
c=(12,23,34,43,56,45,36,54,57,78,59,14,25,"ALI","Sajad")
print(c)
print("IT IS USED TO CHECK 23 VALUE HAVE:::",23 in c) #it used to check if value have so YES and not have so ans is FALSE
print("IT IS USED TO DESCRIBE VALUE 50 have:::",50 in c)#false ans are not have
print("\n 5. find the maximum number of the length ")
d=(1,2,3,4,5,45,46,99,786,987,459,1008,3005,10) #find the maximum number.
print(d)
print("it tells the maximum number is:",max(d))
print("\n 6. It tells the minimum number of the length")  
e=(23,34,24,25,56,35,65,35,3,2,4,5,7,0,3,300,4000,345,2124)
print("\n  it tells the minimum number of the value:",min(e))
print(e) #find the minimum number
f=(1000,1322,1233,999,2993,24234,523423,454,6555,355)
print("it tells the maximum number of the length", max(f))
print("it tells the minimum number of the length", min(f))
print("\n 7. It is used to sum the value ")
g=(20,10,30,40,50,60,1000,1100,1500,2000,5000)
print("the value of g is :",g) #IT IS USED TO SUM THE VALUE OF ALL VALUE
print ("the sum of the value is :",sum(g))
h=(1000,20000,30000,4000,50000,2000,2999,1001)
print("the value of h is: ",h)
print("the sum of value h is:" ,sum(h))
print("\n 8. it is used for scilicing")
i=(1,2,3,34,35,45,36,345,554,37,32,253,575)
print("the value of I is:",i)
sliced=i[1:5] #IT IS USED TO PRINT THE SPECIFIC VALUE PRINT SO WE USED SCILING
print("it is used for specific value print:",sliced)
print("\n 9. unpacking the value")
ji=(23,24,234,"PAKISTAN","Lahore","Sargodha","SIALKOT",45453,2434,45)
print("THE VALUE OF J PRINT:",ji) #they are individual print the data
a,b,c,d,e,f,g,h,i,j = ji
print(a,b,c,d,e,f,g,h,i,j)