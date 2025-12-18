friends=["Apple","Orange",5,345.06,False,"Aakash","Rohan"]

print(friends)

friends.append("Akshansh")
print(friends)

#extend()

lst = [1, 2]
lst.extend([3, 4])
print(lst)

#insert()-Inserts an element at a specific position.
lst = [1, 2, 4]
lst.insert(2, 3)
print(lst)

#remove()-Removes the first occurrence of a value.

lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)

#pop()-Removes and returns the element at a given index (last by default).
lst = [10, 20, 30]
lst.pop()
print(lst)

#index()-Returns the index of the first occurrence of a value.
lst = [10, 20, 30]
print(lst.index(20))

#count()-Counts how many times an element appears.

lst = [1, 2, 2, 3]
print(lst.count(2))

#sort()-Sorts the list in ascending order.
lst = [3, 1, 2]
lst.sort()
print(lst)

#reverse()-Reverses the list order.
lst = [1, 2, 3]
lst.reverse()
print(lst)

#copy()-Creates a shallow copy of the list.
lst = [1, 2, 3]
new_lst = lst.copy()