"""เนับเลขคู่และเลขคี่"""
even = 0
odd = 0

a = int(input())
if not a % 2:
    even += 1
else:
    odd += 1

b = int(input())
if not b % 2:
    even += 1
else:
    odd += 1

c = int(input())
if not c % 2:
    even += 1
else:
    odd += 1

print(even)
print(odd)
