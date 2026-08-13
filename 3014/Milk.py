"""Milk"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

milk = d // a

if not b:
    print(milk)
else:
    caps = milk
    total = milk

    while caps >= b:
        free = (caps // b) * c
        total += free
        caps = (caps % b) + free

    print(total)
