a = "hello World!"
print(a[2:])
print(a[2:4])
print(a[-4:-2])
print(a[-2:-4]) #Doesnot work


print(a.replace("h", "L"))
print(a.lower())

print(a.strip())

print(a.split(" "))

b="hell hwllo"

c = a+b
print(c)

c = a + "combine" +b
print(c)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))