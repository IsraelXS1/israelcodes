print("hello world")

name = "abraham"
print(name)

x = 3
y = 8
sum = x + y
print(sum)

fruits = ["apple", "orange", "carrots", "banana"]
print(fruits)

x = 2.6
y = 1
a = float(y)
print(a)

x = "israel"
print(x[4], x[5])
print(len(x))
for i in range(len(x)):
    print(x[i])

products = ["laptops", "desktops", "phones", "accessories", "smart watches", "tablets", "ipads"]
print(products)
print(products[-1], products[3], products[5])
print(products[2:5])
products[1], products[3], products[5] = "smart glasses", "chains", "books"
print(products)
products.append("chargers")
print(products)
products.insert(5, "books")
print(products)
products.remove("chains")
print(products)
products.pop(3)
print(products)
del products[5]
print(products)
products.clear()
print(products)
products = ["laptops", "desktops", "phones", "accessories", "smart watches", "tablets", "ipads"]
for x in products:
    print(x)

newlist = []

for x in products:
    if "a" in x:
        newlist.append(x)
        print(newlist)
products.sort(reverse=True)
print(products)
myproducts = products.copy()
print(myproducts)

products = ["laptops", "desktops", "phones", "accessories", "smart watches", "tablets", "ipads"]
food = ("rice","beans","spagheti")

product={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : "2003",
    "colour" : "white"
 }
print(product)

print(product["brand"])

print (len(product))
x=product["year"]
print(x)

product["brand"] = "toyota"
print(product)
product.update({"colour": "red"})
print (product)
product.pop("colour")
product.popitem()
print (product)
for x in product:
    print(x)

num1=100
num2=100
if num1 > num2:
    print("number1 is greater than number2")

elif num2 > num1:
    print("number2 is greater than number1")
else:
     print("number1 and number2 are equal")


age=21
if age > 17:
    print("eligible to vote")
else:
    print("not eligible to vote")

x= 0
while x <= 10:
    x+=1

    print (x)
    if x==5:
     continue
    print (x)


def my_function():
    print("my first pyhton function")
my_function()

def my_names(fname):
    print(fname + " isaac" )
    print(fname + " israel")
    print(fname + " abraham")
my_names("my first name is")





