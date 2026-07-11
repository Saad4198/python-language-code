#Write a program to calculate the factorial of a given number using for and while loop.
n=int(input("ENTER THE NUMBER:"))
product=1
for i in range(1,n+1):
    product=product*i
print(f"the factorial of {n} is {product}")
# by using while loop
o=int(input("enter the number:"))
p=1
i=1
while(i<=o):
    p=p*i
    i=i+1
print(f"the factorial of {o} is {p}")
print(f"the factorial of {o} is {p}")