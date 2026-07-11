#Write a program to print multiplication table of a given number using while loop.
n=int(input("ENTER THE NUMBER"))
i=1
while(i<=10):
    print(f"{n}X{i}={n*i}")
    i=i+1