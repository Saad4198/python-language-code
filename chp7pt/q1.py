#Write a program to print multiplication table of a given number using for and while loop.
n=int(input("Enter the value:")) #take input value
for i in range(1,11): #using for loop to check the range
    print(f"{n}X{i}={n*i}") #print the reult of table
    

print("\nWHILE LOOP USED")

j= int(input("Enter the number:"))
k=1
while(k<=10):
    print(f"{j}*{k}={j*k}")
    k=k+1