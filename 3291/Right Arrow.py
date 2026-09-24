"Right Arrow"
k = int(input())
n = int(input())

middle = n // 2

for i in range(n):
    if i <= middle:
        space = i
    else:
        space = n - 1 - i

    print(" " * space + "*" * k)
  
