tup1 = ("sing", "song", "dance", "play")
print(tup1)
print(tup1[0]) # Indexing is allowed
print(tup1[-1], tup1[-2]) # Accessing in the reverse order
print(tup1[1:3]) # tuple slicing
if "play" in tup1:
    print(True)
print("Address before adding", id(tup1))
# Add tuple to tuple
tup1+= ('trek',)
print(tup1)
print("Address after adding", id(tup1)) # new variable is created

tup2 = ("dancer", "singer", "player", "sing")
tup3 = tup1 + tup2
print("Merged/Extended tuples", tup3)

print("Count if dancer and sing", tup3.count('dancer'), tup3.count('sing'))

print("index of sing",tup3.index('sing') )
# Unpacking tuples
(ele1, ele2, ele3, ele4, ele5) = tup1
print("Unpacking - ", ele1, ele2, ele3, ele4, ele5)

(ele1, ele2, ele3) = tup1 #it doesnot wrap the last element to rest in the tuple we need to give the exact number of elements
print(ele1, ele2, ele3)
#tuples are ordered
tup1.append("hike") # cannot append due to immutability
print(tup1)
tup1[0] = "cool" # Random write is not allowed - as it is IMMUTABLE - #type error
print(tup1)




