import csv

def foo():
    pass

class Bar:
    pass

blah = 47

print(type(csv), type(foo), type(Bar), type(blah))

print(dir(Bar))
print(Bar)
print(Bar.__str__(Bar))
b = Bar()
print(b)
print(Bar.__str__(b))
print()

print(dir(csv))
