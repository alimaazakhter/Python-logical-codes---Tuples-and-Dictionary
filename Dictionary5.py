#write a program to multiply all the items in the dictionary
a = {"a" : 1, "b" : 2, "c" : 3, "d": 4, "e" : 5}
print(a)
product = 1
for i in a :
    product *= a[i]
print(product)  
