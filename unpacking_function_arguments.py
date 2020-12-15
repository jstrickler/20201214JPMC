
def spam(a, b, c):
    print(a)
    print(b)
    print(c)
    print()


spam(1, 2, 3)
spam('x', 'y', 'z')

data = [5, 10, 15]

# spam(data)
spam(data[0], data[1], data[2])
spam(*data)

r = reversed(data)
print(r)

print(next(r))
print(next(r))

words = ['alpha', 'beta', 'gamma']

iwords = iter(words) # retrieve iterator from iterable
print(next(iwords))
print(next(iwords))
print(next(iwords))
print()

with open('DATA/knights.csv') as knights_in:
    header = next(knights_in)
    print("header:", header)
    for line in knights_in:
        print(line.rstrip())




