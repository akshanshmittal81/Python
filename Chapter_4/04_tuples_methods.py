a=(1,33798.3,7,"Rohan",False,"Shivam")
print(type(a))
print(a)

#Most Used Tuple Methods in Python

#1. count()-Returns the number of times a value appears in the tuple.

t = (1, 2, 2, 3)
print(t.count(2)) 

#2. index()-Returns the index of the first occurrence of a value.

t = (10, 20, 30)
print(t.index(20)) 

#3. len()-Returns number of elements in the tuple.

t = (1, 2, 3)
print(len(t))

#4. Membership (in / not in)-Checks if an element exists.

t = (1, 2, 3)
print(2 in t)

#5. Slicing-Access a range of elements.

t = (10, 20, 30, 40)
print(t[1:3])

#6. Tuple Concatenation (+)-Joins two tuples.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

#7. Tuple Repetition (*)-Repeats elements.

t = (1, 2)
print(t * 3)

#8. Unpacking-Assigns tuple values to variables

t = (10, 20, 30)
a, b, c = t
print(a,b,c)