"""
In this file we learn about break ,continue and pass
(i). BREAK:
break keyword are used when wee give condition if match so the program stop working and run value before the value match and if not match so they run complete data.
(ii).CONTINUE:
 continue keyword are used if we give the condition and they match and the value match so they skip value and continue after the value give just the condition value 2 and they skip and forward (1,3,4 and so on).
 (iii). PASS:
 pass keyword are used when we used different loops and when we are working one loop and stop working and then used second loop so we used pass e.g if we used for loop and write pass and the write while loop.
"""
#1. break 
print("break ")
for i in range (100):
    if(i==33): # the condition match so they break the statement before value execute and run
        break
    print(i)
#2. continue
print("\n continue")
for i in range(50):
    if(i==33): # the condition match so they continue the statement skip value of bracket before and after value execute and run
        continue
    print(i)

#3. pass keyword
print("\n Pass")
for i in range(50):
    pass
i=0
while(i<50):
    print(i)
    i=i+1
