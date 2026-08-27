"""จำนวนสระ"""
n = int(input())
count = 0

while n > 0:
    ch = input().upper()
    if ch in {'A', 'E', 'I', 'O', 'U'}:
        count += 1
    n -= 1

print(count)
