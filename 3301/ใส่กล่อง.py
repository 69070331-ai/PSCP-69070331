"ใส่กล่อง"
W, L, M, N = map(int, input().split())

minimum = 10**30

for A in range(M, N + 1):
    waste = (W % A) * (L % A)

    if waste < minimum:
        minimum = waste

print(minimum)
