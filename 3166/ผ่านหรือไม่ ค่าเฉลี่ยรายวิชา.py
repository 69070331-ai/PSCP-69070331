"ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"
n = int(input())

total = 0
passed = True

for _ in range(n):
    score = int(input())
    total = total + score

    if score < 50:
        passed = False

average = total / n

print(f"{average:.1f}")

if average < 60:
    passed = False

if passed:
    print("PASS")
else:
    print("FAIL")
