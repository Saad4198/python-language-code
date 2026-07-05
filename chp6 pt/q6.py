# Write a program to calculate the grade of a student from his marks
m=int(input("Enter the marks"))
if (m > 100 or m < 0):
    gr="Invalid marks"
elif(m<=100 and m>=90):
    gr="A+"
elif(m<=90 and m>=80):
    gr="A"
elif(m<=80 and m>=70):
    gr="B"
elif(m<=70 and m>=60):
    gr="C"
elif(m<=60 and m>=50):
    gr="D"
elif(m<=50 and m>=40):
    gr="F"
else:
    gr="fail"
print("YOUR MARKS IS:",m ,"your grade is:",gr)

#2ND METHOD TO SOLVE THESE PROGRAM
print("\n 2ND PROGRAM")
n=m=int(input("Enter the marks")) #value take from the user.
if(n>100 or n<0):
    grade="invalid number"
elif (n >= 90):
    grade = "A+"
elif (n >= 80):
    grade = "A"
elif (n >= 70):
    grade = "B"
elif (n >= 60):
    grade = "C"
elif (n >= 50):
    grade = "D"
elif (n >= 40):
    grade = "F"
else:
    grade="FAIL"

print("YOUR MARKS IS:",n, "your grade is:",grade)