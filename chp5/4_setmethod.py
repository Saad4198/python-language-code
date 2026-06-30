"""
PROPERTIES OF SET:
i. unordered (order does not matter)
ii. there is no way to change the item (means we can remove or change the data in the set).
iii. set cannot duplicate value.
iv.set cannot unindexed (it means we cannot find the index of the any value in the data.)
"""
"""
In set we are used to show different type of data to represent
"""
s={1,2,3,43,32,34,23,32,43,2,3,"SGD","Saad",}
print(s)
print(type(s)) #it tells which type of data are used
#Methods
#Reptition(repeat) value are not allowed
s.add(786) # Add the value in the set.
print("\n 1. Add value 786: ",s)
# 2. remove()
# It removes the given value from the set.
# If the value is not found, Python gives an error.
s.remove(43)
print("\n2. Remove value 43:", s)
# 3. discard()
# It value found so they removes the given value from the set.
# If the value is not found, it does not give an error and print the value same the data are have.
s.discard(100)
print("\n3. Discard value 100:", s)
s.discard(32)
print("Discard value 32:",s)
# 4. pop()
# It removes one random value from the set.
# We cannot choose which value will be removed.
print("\n4. Remove one random value:", s.pop())
print(s)
# 5. copy()
# It creates a copy of the set.
new_set = s.copy()
print("\n5. Copy of the set:", new_set)
# 6. clear()
# It removes all values from the copied set.
new_set.clear()
print("\n6. Clear copied set:", new_set)
# 7. update()
# It adds multiple values to the set.
s.update([500, 600, 700])
print("\n7. Add multiple values:", s)
# 8. union()
# It joins two sets and returns a new set.
s2 = {800, 900, 1000}
print("\n8. Union of two sets:", s.union(s2))
# 9. intersection()
# It prints only the common values from both sets.
a = {1,2,3,4}
b = {3,4,5,6}
print("\n9. Intersection of two sets:",a.intersection(b))
















