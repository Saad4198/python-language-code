#write some message used for spam
#first program
print("First program:")
a="make a lot of money" 
b="buy now"
c="subscribe this"
d="click this"
m=input("Enterr the message:")
m=m.lower()
if((a in m) or (b in m) or (c in m) or (d in m)):
    print("Spam message:",m)
else:
    print("Not a spam message:",m)

#2nd program with multiple spam message
#the mulitple message thar are used for spam
print("\n 2nd program:")
me=input("Enter the message:")
me=me.lower()
if("make a lot of money" in me):
    print("spam message:",me)
elif("buy now" in me):
    print("spam message:",me)
elif("subscribe this" in me):
    print("spam message:",me)
elif("click this" in me):
    print("spam message:",me)
elif("click here" in me):
    print("spam message:",me)
elif("win a prize" in me):
    print("spam message:",me)
elif("congratulations! You won" in me):
    print("spam message:",me)
elif("free gift" in me):
    print("spam message:",me)
elif("free money" in me):
    print("spam message:",me)
elif("earn money fast" in me):
    print("spam message:",me)
elif("limited time offer" in me):
    print("spam message:",me)
elif("claim your reward" in me):
    print("spam message:",me)
elif("cash prize" in me):
    print("spam message:",me)
elif("get rich quick" in me):
    print("spam message:",me)
elif("100% free" in me):
    print("spam message:",me)
elif("exclusive offer" in me):
    print("spam message:",me)
elif("lowest price" in me):
    print("spam message:",me)
elif("special discount" in me):
    print("spam message:",me)
elif("hurry up" in me):
    print("spam message:",me)
elif("act now" in me):
    print("spam message:",me)
elif("lucky winner" in me):
    print("spam message:",me)
elif("you have been selected" in me):
    print("spam message:",me)
elif("free iphone" in me):
    print("spam message:",me)
elif("earn $1000 per day" in me):
    print("spam message:",me)
elif("free laptop" in me):
    print("spam message:",me)
elif("double your money" in me):
    print("spam message:",me)
elif("investment opportunity" in me):
    print("spam message:",me)
elif("no investment required" in me):
    print("spam message:",me)
elif("guaranteed income" in me):
    print("spam message:",me)
elif("instant cash" in me):
    print("spam message:",me)
elif("easy money" in me):
    print("spam message:",me)
elif("work from home" in me):
    print("spam message:",me)
elif("verify your account" in me):
    print("spam message:",me)
elif("login now" in me):
    print("spam message:",me)
elif("download now" in me):
    print("spam message:",me)
elif("register now" in me):
    print("spam message:",me)
elif("claim now" in me):
    print("spam message:",me)
elif("congratulations! claim your prize" in me):
    print("spam message:",me)

else:
    print("The message is not spam message:",me)