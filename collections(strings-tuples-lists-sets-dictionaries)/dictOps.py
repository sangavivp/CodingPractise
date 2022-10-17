thisDict = {}
thisDict['brand'] = "Ford"
thisDict['model'] = "Mustag"
thisDict['year'] = 1994

print(thisDict['model'])

print(thisDict.get("model"))

print(thisDict.keys())



print(thisDict.values())

print(thisDict.items())

if "model" in thisDict:
    print('Key is found - True')

if 'BMW' in thisDict:
    print('Value can be found')
else:
    print('Value cannot be found')

if "model" in thisDict.keys():
    print(True)


thisDict['brand'] = "BMW"

thisDict.update({'model': 'Renault'})
print(thisDict)

# thisDict.update(['model', 'Renault']) #Doesnot work
# print(thisDict)

print("Key in the dictionaries Printing")
for x in thisDict:
    print(x)

for x in thisDict:
    print(thisDict[x])

for x in thisDict.values():
    print(x)

for x,y in thisDict.items():
    print(x, y)

thisDictCopy = thisDict.copy()
thisDictCopy2 = dict(thisDict)

print(id(thisDict))
print(id(thisDictCopy))
print(id(thisDictCopy2))








print(thisDict.pop("year"))
print(thisDict)

print(thisDict.popitem())
print(thisDict)

del thisDict["model"]
print(thisDict)

thisDict.clear()
print(thisDict)

del thisDict
print(thisDict)


