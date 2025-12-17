name="Akshansh"
print(len(name))
print(name.endswith("sh"))
print(name.startswith("aks"))
print(name.capitalize())#capital only fisrt character first word 
print(name.lower())
print(name.upper())
print(name.title())#capitalize first character of every word in a string
print(name.swapcase())


#Trimming & Whitespace Removal

s="   python   "
print(s.strip())#Removes leading & trailing spaces
print(s.lstrip())#Removes leading spaces
print(s.rstrip())#Removes trailing spaces

#Search & Check Methods
s1="python programming"
print(s1.find("programming"))#Returns first index or -1
print(s1.index("python"))#Returns index or raises error
print(s1.count("python"))
#endwith and startswith

##String Testing / Validation Methods

s2= "Python123"
print(s2.isalnum())#Letters + numbers only
print(s2.isalpha())#Letters only
print(s2.isdigit())#Digits only
print(s2.islower())#All lowercase
print(s2.isupper())#All uppercase
print(s2.isspace())#Only whitespace

#Replace & Modify Strings functions

s3= "I like Java"
a=s3.replace("Java", "python")
print(a)

#Splitting & Joining Strings functions
s4= "apple,banana,orange mango " 
print(s4.split(','))#Splits string into list
print(s4.rsplit())#Splits from right
print(s4.splitlines())
b=s4.split(',')
c='#'.join(b)
print(c)

##Formatting Strings functions

name='Akshansh'
print("hello {}".format(name))
print(f"Hello {name}")

#Alignment & Padding functions

s5="Python"
width=10
print(s5.center(width))
print(s5.ljust(width))
print(s5.rjust(width))
print(s5.zfill(width))

##Encoding & Decoding functions

e=s5.encode()
print(e)
f=e.decode()
print(f)
