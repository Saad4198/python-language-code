"""
write a program that take subject marks from the user if it requires a total of
40% and at least 33% in each subject to pass. 
"""
a=int(input("Enter your subject marks:")) # enter the subject marks
b=int(input("Enter your subject marks:")) # enter the subject marks   
c=int(input("Enter your subject marks:")) # enter the subject marks 
d=int(input("Enter your subject marks:")) # enter the subject marks
totper=100*(a+b+c+d)/400   #totper means total_percentage
print("The percentage are:",totper)
if(totper>=40 and a>=33 and b>=33 and c>=33 and d>=33):
    print("you are passed:",totper)
else:
    print("you are failed:",totper)