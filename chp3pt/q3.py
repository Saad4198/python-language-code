"""
this is used to find any data in double quotes to find data or space so we used find function and if data or space or not found so we used -1 value give means data are not found and if data found so it give ans according to it index value
"""
name= "Hello how are you  i hope you are fine"
print(name)
print(name.find("  ")) # value found at index 17 
print(name.find("ALI")) #value not found beacuse ali are not have name variable value are not have.
value="12 34 56 77 8990"
print(value)
print(value.find("56")) #they are found at index 6
print(value.find("786")) #786 data are not found so it give ans -1.