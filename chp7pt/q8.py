"""
Write a program to print the following star pattern.
*
***
***** for n = 3
imp!
1.the print("") these are used to print the data in the new line
2. end= are represent because every print give the new line so we used because the data are print in same line the output you check first print has two space and then new print the value so we used end= print the data in the same and at the end the empty that are used to complete one time data and then print the data in the new line  

"""
n=int(input("enter the number:"))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")