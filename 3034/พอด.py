"""พอด"""
N, K = map(int, input().split())

queue = [0] * K

for _ in range(N):
    row = int(input())
    queue[row - 1] += 1

rounds = min(queue)
remaining = N - (rounds * K)

print(remaining)
