#first program by using these structure
#(if + elif + elif + else) these structure used
#you take age from the user and print data according.

print("THE FIRST PROGRAM")
a=int(input("ENTER YOUR AGE:")) 
if(a<13): #enter the age less than 13
    print("you are CHILD" )

elif(a<20): #enter the age less than 20
    print("you are TEENAGER")

elif(a<60): #enter the age less than 60
    print("you are  ADULT:")

else: #enter the age greater than 60
    print("you are senior citizen")

print("THE FIRST PRGRAM ARE NOW END")

#Second program by using these structure
#(if + elif + elif + elif + else) these structure used
print("\nTHE SECOND PROGRAM") # t represent the temp variable
t=int(input("Enter the temperature:"))
if(t<0):
    print("freezing")

elif(t>=1 and t<=20):
    print("temperature are cold:",t)

elif(t>=21 and t<=35):
    print("temperature are warm:",t)

elif(t>=36 and t<=45):
    print(" temperature are hot:",t)

else:
    print("temperature are very hot",t)

print("THE SECOND PROGRAM ARE NOW END")
#third program when many if statement are have
#structure: if-if-elif-else.
print("\nTHe third program are now start")
v=int(input("Enter the value:"))

if(v%2==0):
    print("YOU ENTER THE EVEN NUMBER:",v)

if(v>0):
    print("you enter the positive number: ",v)

elif(v==0):
    print("you enter the number are zero:",v)
elif(v<0):
    print("you enter the number are negative:",v)
else:
    print("you enterr the invalid number",v)