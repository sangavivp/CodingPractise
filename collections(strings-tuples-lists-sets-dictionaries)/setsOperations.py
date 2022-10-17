# https://www.w3schools.com/python/python_sets_methods.asp

myset = {'apple', 'carrot', 'orange', 'lemon', 'strawberry'} # Unordered/unchangeable/unindexed

myset2 = set(('apple', 'carrot', 'orange', 'lemon', 'strawberry', 'strawberry'))

print(len(myset))

print(id(myset))
for x in myset:
    print(x)


# for i in range(len(myset)):  # Not allowed for sets - TypeError
#     print(myset[i])


myset.add('mango') # to add a element to the set

myset.update(myset2)
print(myset)
print(id(myset)) # We can extend the set but we cannot change the elements in the list



mylist = ['kiwi', 'grapefruit']
myset.update(mylist)
print(myset)
print(id(myset))


myset3 = myset.union(myset2)

print("Union", myset3)

myset3.intersection_update(myset2)
print("Duplicates set", myset3)
myset4 = myset3.intersection_update(myset2)
print("Duplicates as a separate set", myset4)

# Excluding the common set
# myset4.symmetric_difference_update(myset2)
# print(myset4)
myset5 = myset4.symmetric_different(myset2)
print(myset5)



myset.remove('kiwi')
print(myset)

myset.discard('kiwi')
# myset.remove('kiwi') # This will throw an error as it not present in the set now

print(myset.pop()) # Last element - as its unordered anything at the moment in the last element will be removed
print(myset)


myset.clear()
print(myset)

del myset
print(myset)

