"Arrow"
d = input()
n = int(input())

for direction in d:
    for i in range(2 * n - 1):
        level = min(i, 2 * n - 2 - i)
        star = n - level

        if direction == "R":
            space = level * 2
        else:
            space = n - 1 - level

        print(" " * space + "*" * star)

    print()
