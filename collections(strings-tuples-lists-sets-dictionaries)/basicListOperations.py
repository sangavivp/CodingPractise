list1 = [1, 2, 3]
list2 = ['try', 'many','things']
print(list1+list2) # Returns the new list
list1.append(list2) # appends as a list
print(list1)
list1.extend(list2) # appends as elements same as + but modifies the existing list
print(list1)
list1+=list2 # appends as elements same as +
print(list1)

print(list1[1:4])
print(list1[-4:-1])

print(list1.pop(0)) # Pop returns element that's popped out
print(list1.pop(3))

print(list1)