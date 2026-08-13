"""คะแนนสอบ"""
n = int(input())

max_score = 0
count = 0

while n > 0:
    score = int(input())

    if score > max_score:
        max_score = score
        count = 1
    elif score == max_score:
        count += 1

    n -= 1

print(max_score)
print(count)
