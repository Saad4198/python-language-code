#In conditional if ,ifelse , and elif writee after condition we wrtie colon: if we not write so give they error.
#First program by using if condition
print("\n FIRST PROGRAM:")
print("BY using IF CONDITION")
a=int(input("Enter your age:"))
if(a>18): #the age are enter greater than 18
    print("YOU ARE ELIGIBLE FOR LICENSE")
#Second program by using if else condition
print("\n Seocnd PROGRAM")
n=int(input("Enter the number"))
if(n%2==0):
    print("you enter the number is even:",n)

else:
    print("you enter the odd number:",n)

#Third program BY using if elif else  condition
#to enter marks and check the grade of your subject
c=int(input("\nEnter the number of your subject:"))
if(c>=80):
    print("your grade of your marks are A:",c)

elif(c>=50):
    print("your grade of your marks are B:",c)

else:
    ("YOU ARE FAIL:",c)
