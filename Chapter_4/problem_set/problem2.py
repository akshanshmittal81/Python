# Write a program to accept marks of 6 students and display them in a sorted manner.
#Write a program to store seven fruits in a list entered by the user.

marks=[]

m1=int(input("Enter marks: "))
marks.append(m1)
m2=int(input("Enter marks: "))
marks.append(m2)
m3=int(input("Enter marks: "))
marks.append(m3)
m4=int(input("Enter marks: "))
marks.append(m4)
m5=int(input("Enter marks: "))
marks.append(m5)
m6=int(input("Enter marks: "))
marks.append(m6)

marks.sort()

print(marks)