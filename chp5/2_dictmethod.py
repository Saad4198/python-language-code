"""
Methos of dict:
i. unordered ii. mutuable(add or change data)
iii.indexed  iv.cannot take duplicate value.
"""
#METHODS OF DICTIONARY
name = {
 "Saad":100,
 "lahore":24563,
 "islamabad" :23232,
 "pakistan":14081947,
 "list":[1,2,3,232,2324,13134,67567],
  0:"saad"
}
#print all the data
print("1. print all the data:",name) #print all the data
#print all the data in tuple form
print("\n2. PRINT THE ITEM :",name.items()) #it print the items in tuple form 
#it print all the key value in dictionary.
print("\n3. PRINT THE KEYS OF THE VALUE:",name.keys()) #it prints the keys of items we check the item of the key of data.
print("\n4. PRINT THE VALUE OF KEY:",name.values()) #it prints the value of the key in the data
print("\n5. THEY ARE UPDATE VALUE IN DICT:",name.update({"Saad":95, "ALI":75,"Shamir":70}))
print("\n6. The update value in key:",name)#the value are update so they are show.
#if key have so value give otherwise none give
print("\n 7.Give value of Saad:",name.get("Saad")) #value give of saad because it have 
print("8. Give the value of ahmed if have:",name.get("ahmed")) #it give none because ahmed key are not have.
print(name["Saad"]) #if value not found so error give otherwise key value give.
# 9. pop()
# It removes the given key from the dictionary and returns its value.
print("\n9. Remove the key:")
print("\nRemove the value",name.pop("lahore"))   # Remove the key and print its value.
print(name)                 # Print the updated dictionary.
#print(name.pop("islambad")) remove the key islamabad
#print(name)
# 10. popitem()
# It removes the last key-value pair from the dictionary.
print("\n10. Remove the last item:")
print("Remove the last item:",name.popitem())       # Remove and print the last item.
print(name)                 # Print the updated dictionary.
# 11. copy()
# It creates a copy of the dictionary.
print("\n11. Copy the dictionary:")
new_name = name.copy()      # Make a copy of the dictionary.
print(new_name)             # Print the copied dictionary.
# 12. setdefault()
#if value are not have so they add in key 
# If the key exists, it returns its value.
# If the key does not exist, it adds the key with the given value.
print("\n12. Set default value:")
print("Add value in dict",name.setdefault("Country", "Pakistan"))  # Add a new key.
print(name)
# 13. fromkeys()
# It creates a new dictionary using the given keys and one common value.
#in KEYS A,B,C value are 0 because it values are not assign.
print("\n13. Create a new dictionary using fromkeys():")
keys = ("A", "B", "C") 
new_dict = dict.fromkeys(keys, 0)
print(new_dict)
# 14. len()
# It counts the total number of key-value pairs.
print("\n14. Count total items:")
print("Tells the length ",len(name))
# 15. in
# It checks whether a key exists in the dictionary.
# if have value so give TRUE otherwise False.
print("\n15. Check if 'Saad' key exists:")
print("Check the Saad value have","Saad" in name)
print("Check the Ahmed value have","Ahmed" in name)
# 16. clear()
# It removes all items from the dictionary.
# it complete clear all the dict.
print("\n16. Clear the copied dictionary:")
name.clear()            # Delete all items from the copied dictionary.
print(name)             # Output: {}
