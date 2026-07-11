#Write a program to find the sum of first n natural numbers using while and for loop
n=int(input("Enter the number:"))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1

print(sum)
#2nd method by using for loop
k=int(input("ENter the second number:"))
j=1
s=0
for j in range(1,k+1):
    s=s+j
    j=j+1
print(s)