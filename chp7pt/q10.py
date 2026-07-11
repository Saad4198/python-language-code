#to print the table in reverse order of for and while loop
n=int(input("enter the number:"))
for i in range(1,11):
    print(f"{n}X{11-i}={n*(11-i)}")


print("\nwhile loop")
j=int(input("enter the number:"))
k=10
while(k>=1):
    print(f"{j}X{k}={j*k}")
    k=k-1

