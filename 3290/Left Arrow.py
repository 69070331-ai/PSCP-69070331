"Left Arrow"
k = int(input())
n = int(input())

middle = n // 2

for i in range(n):
    space = abs(middle - i)
    print(" " * space + "*" * k)
