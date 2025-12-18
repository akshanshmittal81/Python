letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Take inputs from the user
name = input("Enter your name: ")
date = input("Enter the date: ")

# Replace placeholders with actual values
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

# Print the final letter
print(letter)






