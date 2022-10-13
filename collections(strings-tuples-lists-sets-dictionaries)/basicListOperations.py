list1 = [1, 2, 3]
list2 = ['try', 'many','things']

print(list1+list2) # Returns the new list
list1.append(list2) # appends as a list

print('inserting elements', list1.insert(1, 'inserting'))
print(list1)
list1.extend(list2) # appends as elements same as + but modifies the existing list
print(list1)
list1+=list2 # appends as elements same as +
print(list1)
print(list1[1:4])
print(list1[-4:-1])
print(list1)

# list slicing
print(list1[2: 4])
#updating the slice
list1[2:4] = ["simple", "test"]
print(list1)
list1[2:4] = ["simple2"] # 2 and 3rd element gets replaced by 'simple2'
print(list1)

## List comprehension
print("List comprehension")
[print(x) for x in list1]

[print(x) for x in list1 if x is 'many']

[print(x) if x != 'try' else "nothing" for x in list1 ] # handling if-else with list comprehension

### https://www.w3schools.com/python/python_lists_sort.asp for 13 Oct
print("Sorting\n\n")

# list1.sort() # Works only on Homogenous types
list3 = ['try', 'many','things', 'for', 'NOw', 'Later', 'SOON']
print(list3)
list3.reverse()
print(list3)
list_num = [9, 6, 4, 5, 0]

def closeness_fun(num):
    return abs(num-0)

list_num.sort(key=closeness_fun)

print(list_num)

list3.sort(key = str.lower)
print(list3)

list3.sort(reverse=True)
print(list3)


## Copying List
list5 = list3 # Reference is copied
print(id(list5))
print(id(list3))


list6 = list3.copy() # independent copies
print(id(list6))
print(id(list3))
list3[3] = 'hello'
print(list6)
print(list3)

list7 = list(list3) # independent copies
print(id(list7))
print(id(list3))


# removing
print("\n\nremoving and popping")
list1.remove('many') # doesnot return but changes the list1
list1.remove('things')
list1[4].remove('many')
list1.remove(1)
print(list1)
print(list1.pop(0)) # Pop returns element that's popped out
print(list1.pop(3))
print(list1.pop()) # last element
# clear and del
del list1[0]
print(list1.clear())
del list1
print(list1) # Name error as the list is not present