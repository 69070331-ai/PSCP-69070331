"""รหัสสเเฝดเทค"""
N = int(input())
a = input()
b = input()

count = 0

for i in range(N):
    if int(a[i]) + int(b[i]) != 9:
        count += 1

if not count:
    print("YES")
else:
    print("NO", count)
