"ระบบคิดคะแนนเกมออนไลน์"
base = int(input())
bonus = int(input())
days = int(input())

score = base + bonus

if days > 3:
    score = int(score * 1.5)

if score >= 1500:
    RANK = 5
elif score >= 1000:
    RANK = 4
elif score >= 500:
    RANK = 3
elif score >= 200:
    RANK = 2
else:
    RANK = 1

if RANK == 5 and days >= 7:
    STATUS = 99
elif RANK == 4 and bonus > 300:
    STATUS = 88
else:
    STATUS = 0

print(score)
print(RANK)
print(STATUS)
