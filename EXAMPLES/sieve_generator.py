#!/usr/bin/env python

def next_prime(limit):
    non_prime = [False] * (limit + 1)LAB
#    non_prime = set()  # <1>

    for i in range(2, limit):
        if non_prime[i]: # in non_prime:
            continue
        for j in range(2 * i, limit + 1, i):
            non_prime[j] = True
 #           non_prime.add(j)  # <2>
        yield i  # <3>   returns to next() not to next_prime()


np = next_prime(200)  # <4>
print(np)

# print(next(np))
# print(next(np))
# print(next(np))
# print(next(np))


for prime in np:  # <5>
    print(prime, end=' ')
print()
