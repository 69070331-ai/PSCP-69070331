"ผลรวมของค่าที่มากกว่า"
n = int(input())

total = 0
result = ""

for i in range(n):
    a = int(input())
    b = int(input())

    big = max(a, b)
    total += big

    if not i :
        result = str(big)
    else:
        result += " + " + str(big)

if n == 1:
    print(result)
else:
    print(result + " = " + str(total))
