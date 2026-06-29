"""
write a program that take marks from the user and sort the number and find the sum of the number
"""
#They are used string and not used datatype only STRING used so they only sort data 1,2,3, not arranged they want.
marks=[]
f1=input("Enter the marks Here:")
marks.append(f1)
f2=input("Enter the marks Here:")
marks.append(f2)
f3=input("Enter the marks Here:")
marks.append(f3)
f4=input("Enter the marks Here:")
marks.append(f4)
f5=input("Enter the marks Here:")
marks.append(f5)
f6=input("Enter the marks Here:")
marks.append(f6)
print("The marks are unsorted form",marks)
marks.sort()
print("\nThe marks are sorted",marks)
#When we usedd data type so the reuslts are of my data 
marks1=[]
print("\n The mrks are take by using data type of INT")
f1=int(input("Enter the marks Here:"))
marks1.append(f1)
f2=int(input("Enter the marks Here:"))
marks1.append(f2)
f3=int(input("Enter the marks Here:"))
marks1.append(f3)
f4=int(input("Enter the marks Here:"))
marks1.append(f4)
f5=int(input("Enter the marks Here:"))
marks1.append(f5)
f6=int(input("Enter the marks Here:"))
marks1.append(f6)
print("The marks of all show",marks1)
marks1.sort()
print("\nThe marks are sorted Form:",marks1)
print("the sum of all marks is:",sum(marks1))
