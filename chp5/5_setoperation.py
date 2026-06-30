"""
In this we learn some operation of set the common operations are: i.union ii. intersection
iii.Difference iv.Symmetric Difference v. Subset Operation vi. Subset Operation 
vii.Disjoint Operation viii. length ix. remove x.pop 
"""
# 1. Union Operation
# It joins two sets and removes duplicate values.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("the value of a set is:",a)
print("the value of b set is:",b)
d={23,34,56}
e={122,23,34,56,78,134}
print("print the value of d:",d)
print("print the value of e:",e)
print("\n 1.Union of two sets a and b is:", a.union(b))
print("Union of two sets d and e is:", d.union(e))
#2.Intersection operation
# it prints the common values on both set
print("\n 2. Intersection of two sections a and b is:",a.intersection(b))
print(" Intersection of two sections d and e is:",d.intersection(e))
# 3. Difference Operation
#It prints the values that are in the first set but not in the second set.
print("\n 3.Difference of two section a and b is:", a.difference(b))
print("Difference of two section d and e is:", d.difference(e))
#4. Symmetric Difference.
 #It prints the values that are not common in both sets.
print("\n 4. Symmetric difference of both sets a and b is:",a.symmetric_difference(b))
print("Symmetric difference of both sets d and e is:",d.symmetric_difference(e))
# 5.Subset operations.
#It checks whether all values of the first set exist in the second set.
#if  value are have so give output TRUE
#if value are not have and not match so give output FALSE
print("\n5.Subset operations of a and b:",a.issubset(b)) #false value are not have.
print("subset operations d and e:", d.issubset(e)) #ANS is TRUE because value of D SET are have E SET.
#6.Superset Operation
# It checks whether the first set contains all values of the second set.
print("\n 6. Is superset of a and b:", b.issuperset(a))
print("Is superset of d and e:", e.issuperset(d))
#7. Disjoint Operations
# It checks whether both sets have no common values.
#if value are same so ouutput FALSE if not same so output is TRUE. 
print("\n7. Disjoint operations of a and b is:",a.isdisjoint(b))
print("Disjoint operrations of d and e is:",d.isdisjoint(e))
print("\n8. length of the set")
print("length of set a:",len(a))
print("length of set b:",len(b))
print("length of set d:",len(d))
print("length of set e:",len(e))
print("\n9. Remove of the set")
a.remove(3)
print("Remove of set a:",a)
b.remove(4)
print("Remove of set b:",b)
d.remove(34)
print("Remove of set d:",d)
e.remove(56)
print("Remove of set e:",e)
#print("Remove of set e:",e.remove(56)) if we used these so they give me output NONE if we used up code so they give me correct code.
print("\n 10. clear of the set ")
a.clear()
print("clear the data of a:",a)
b.clear()
print("clear the set of b is:",b)
d.clear()
print("clear the set of d is:",d)
e.clear()
print("clear the set of e is:",e)
#print("Remove of set e:",e.clear())) if we used these so they give me output NONE if we used up code so they give me correct code.