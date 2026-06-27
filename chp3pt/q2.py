"""
<|department|> THE DATA WRITE IN THESE FORM CALLED PLACEHOLDER AND we used to replace these format so we by using .replace commands so we used who to convert the data
"""

letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>" , "Saad").replace("<|Date|>", "23 june 2026"))

print("\n this is the 2nd example")
address =''' Address <|location|>
you are select for university admission!
<|department|>

'''
print(address.replace("<|location|>", "SGD").replace("<|department|>" , "CS AND IT "))
