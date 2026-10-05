# name=(input("enter your name: "))
# print( input("welcome to our coding"))
# input ("enter yor good name")

print("welcome to codeing")
ourinput= input("enter our good name: ")
print("hi", ourinput ,"how are you ?")

p1 =int(input("enter the prise of frist product: "))
p2 =int (input("enter the prise od second product: "))
p3 =int (input("enter the prise od third product: "))

total = p1 + p2 + p3

print("your total billing is: ", total)
# name=(input("enter your name: "))
# print( input("welcome to our coding"))
# input ("enter yor good name")

print("welcome to codeing")
ourinput= input("enter our good name: ")
print("hi", ourinput ,"how are you ?")

p1 =int(input("enter the prise of frist product: "))
p2 =int (input("enter the prise od second product: "))
p3 =int (input("enter the prise od third product: "))

total = p1 + p2 + p3

print("your total billing is: ", total)



products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for product, price in products.items():
    products[product] = round(price * 0.8)

