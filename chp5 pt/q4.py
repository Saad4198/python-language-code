#write a program that take value form the user and print it length.
s=set()
s.add(18)
s.add(18.2)
s.add("Pakistan")
s.add(101)
s.add(101.0)
s.add(101.1)
print("print all the value of the set:",s)
print("print the length of the set:",len(s))
"""
one important notice is the length if we count so we used total 6 numbers but we print the length so they give me 5 length if the set why?
because the value 101 and 101.0 both are equal in python language they count both number only one time and we print the value so check it give me only one time 101 value.
"""
t=set()
t.add(1100)
t.add(1100.0)
print("\nlength of T Value:",t)
print("length of the t value:",len(t)) 
#it print and count only one time value of both.
a=set()
a.add(100)
a.add(100.9)
a.add(100.1)
a.add(100.2)
print("print the value of a is;",a)
print("the length of a is:",len(a))#it give me four length and print the data of four value.