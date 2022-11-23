c = lambda a : a*a
print(c(5))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2) # just populates one unknown value
print(myfunc(2))
print(mydoubler(6))


lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)


# Lambda function questions - https://www.w3resource.com/python-exercises/lambda/index.php

# Adding 15
def muFunc(k):
    return lambda k: k+15

print(muFunc(4))

# multiplying with unknown number

def muFunc2(n):
    return lambda a:a*n

muFunc3 = muFunc2(2)
print(muFunc3(10))

list2 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list2.sort(key=lambda x:x[1])
print(list2)

#Sorting a list of dictionaries

list4 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
list4.sort(key=lambda x:x['color'])
print(list4)

# Filter based
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda n:n%2 == 0, list5)))
print(list(filter(lambda n:n%2 != 0, list5)))
