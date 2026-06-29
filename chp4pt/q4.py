#write a program the sum of number of different type
a=(123,234,345,456,567,678,789)
print("the sum of value a is",a)
print("the ANS IS:",sum(a))
b=(21.4,23.4,34.6,45.6,49.6,333.9)
print("the sum of value b is ",b)
print("the ANS OF B VALUE IS",sum(b))
c=sum(a)+sum(b)
print("the sum of total value A AND B IS",c)
#write a program that take value user at different datatype and sum of all these 
number=[]
d=int(input("Enter a number:"))
number.append(d)
e=int(input("Enter a number:"))
number.append(e)
f=float(input("Enter a number:"))
number.append(f)
g=float(input("Enter a number:"))
number.append(g)
print("the value of D TO G variable value",number)
i=sum([d,e,f,g]) #wee used different datatype and sum of all these
print("the sum of value",i)