#SECOND PROGRAM BY USING THESE STRUCTURE. (if + elif + elif + else)
# to build calculator
b=int(input("ENTER THE 1ST NUMBERR:"))
c=int(input("Enterr the second number:"))
operator=input("enter the operation(+,-,*,%) :")

if(operator=="+"):
    print("sum of both number:",b+c)

elif(operator=="-"):
    print("Subtract of bith number:",b-c)
elif(operator=="*"):
    print("Subtract of bith number:",b*c)
elif(operator=="%"):
    print("Subtract of bith number:",b%c)

else:
    print("you enter the invalid operations")