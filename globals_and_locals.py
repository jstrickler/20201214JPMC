from pprint import pprint

name = "Fred"

colors = ['red', 'green', 'purple']

def spam():
    x = 100
    print(locals())

g = globals()
pprint(g)
print()
spam()
print(g['name'])
g['time_stamp']()
print(g['colors'][-1])

g['dog'] = 'Nellie'  #    dog = 'Nellie'

# print(dog)

