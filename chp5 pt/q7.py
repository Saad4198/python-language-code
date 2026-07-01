"""
in this i have one q if my two friends name and same but different langauge used so they prefer the last language or updateafter first value they give updated value.
just like friend ali and they first enter language python and then same friends put langauge c language so they consider last langauge give they accept.
In python the keys are different. if they are same so some problems are occur in output and result.
"""
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