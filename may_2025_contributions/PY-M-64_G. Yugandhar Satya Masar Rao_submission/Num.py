# This Program is to print their sum, difference, product, and quotient.
a=int(input("Enter a first num:"))

b=int(input("Enter a Second num:"))

def sum(a,b):
    return a+b
print("Sum of given Two numbers :", sum(a,b))

def diff(a,b):
    return a-b
print("Difference of given Two numbers :", diff(a,b))

def prod(a,b):
    return a*b
print("Product of given Two numbers :", prod(a,b))

def quot(a,b):
    return a/b
print("Quotient of given Two numbers :", quot(a,b))

def mod(a,b):
    return a%b
print("Modular divison of given Two numbers :", mod(a,b))

def Flordiv(a,b):
    return a//b
print("Floor divison of given Two numbers :", Flordiv(a,b))

def Expo(a,b):
    return a**b
print("Exponentiation of given Two numbers :", Expo(a,b))


