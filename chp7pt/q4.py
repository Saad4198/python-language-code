#Write a program to find whether a given number is prime or not
#prime number are those they divide by own or itself just like 2,3 5,7,etc
n=int(input("Enter the number:"))
for i in range(2,n):
    if(n%i)==0:
        print("number is not a prime:",n)
        break
else:
     print("number is prime:",n)
    
    #second method
    
