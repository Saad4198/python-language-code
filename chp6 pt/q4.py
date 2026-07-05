#write a program that ask the user to enter the name and length are maximum 10 letter
n=input("ENTER YOUR NAME:") #n represent name variable value
print("the length of the text:",len(n)) #length show in output
if(len(n)<10):
    print("THE Length contains less 10  character:",n)
else:
    print("THE Length contains 10 are more character:",n)
    
print("FIRST PROGRAM END")
#Write a program that asks the user to enter a password. If the password length is at least 8 characters, print "Strong Password". Otherwise, print "Weak Password".
print("\n Seond program")
p=input("Enter the passsword:") #p represent password variable value.
print("Length of the password:",len(p)) #length show in output
if(len(p)>=8):
    print("Strong Password:",p)
else:
    print("Weak password:",p)