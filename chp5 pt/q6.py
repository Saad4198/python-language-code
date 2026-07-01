#create and emoty dictionsty and allow your friends to add your name with your favourite language.
d={}
name=input("Enter your 1st firend name:")
lang=input("Enter your favourite Lang:")
d.update({name:lang})
name=input("Enter your 2nd firend name:")
lang=input("Enter your favourite Lang:")
d.update({name:lang})
name=input("Enter your 3rd firend name:")
lang=input("Enter your favourite Lang:")
d.update({name:lang})
name=input("Enter your 4th firend name:")
lang=input("Enter your favourite Lang:")
d.update({name:lang})
name=input("Enter your 5th firend name:")
lang=input("Enter your favourite Lang:")
d.update({name:lang})
print(d)
"""
2nd methods
    # Create an empty dictionary
friends = {}
print("\n THE 2ND METHOD OF WRITE A CODE")
# Take input from 4 friends
name = input("Enter the name of Friend 1: ")
language = input("Enter favorite language: ")
friends[name] = language

name = input("Enter the name of Friend 2: ")
language = input("Enter favorite language: ")
friends[name] = language

name = input("Enter the name of Friend 3: ")
language = input("Enter favorite language: ")
friends[name] = language

name = input("Enter the name of Friend 4: ")
language = input("Enter favorite language: ")
friends[name] = language

# Print the dictionary
print("\nFriends and their favorite languages:")
print(friends)
"""
