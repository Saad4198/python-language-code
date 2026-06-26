#this topic name is string slicing
name="MSAAD"
print(name[0:3])             #print name index 0 to 2
print(name[-4:-1])          #print name from backside index -4 to-2
#if we convert the negative index to postive so easily understand which data print.
print(name[1:4])    #-4 convert 1 and -1 convert 4 index
print(name[:4])     #if first index are not given so it consider are 0.
print(name[1:])     #if last index are not give so last index -1 are used justlike 5word so ans 4
print(name[0:5])     #they represent all the complete word they are given in name variable.
"""
1. if the three index so we follow these step this is the second part of the negtive scilicing.if we give characterer and find the index of the character and we used the formula to solve these data: string[start : stop : step] start means index from start this position, and end index these position stop and step means position jump . for example a[1:7:3] a is the string name , 1 is start point , 7 is the end point and 3 means jump the position.
2. if the two index are have so we follow these step and formula string[start:stop] strat means start point and stop means ending point in these index the step or jump formula are not have.
the example are solve in down.
"""
#slicing with skip value
a = "0123456789"
print(a[1:7:3])   
 #ans is 14 index 1 value is 1 and index 4 value is 4 and both merge and not index 7 value not take
b = "abcdefghijklmnopqrstuvwxyz"      
 #these are the second state they used index 0 value to index20 value al
print(b[0:20])
