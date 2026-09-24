"Electric_Using"
N = int(input())

if N <= 10:
    electricity = N * 5
elif N <= 50:
    electricity = 10 * 5 + (N - 10) * 7
elif N <= 100:
    electricity = 10 * 5 + 40 * 7 + (N - 50) * 10
elif N <= 200:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + (N - 100) * 12
else:
    electricity = 10 * 5 + 40 * 7 + 50 * 10 + 100 * 12 + (N - 200) * 15

total_satang = electricity * 107 + N * 50

result = (total_satang + 5) // 10

print(result // 10, ".", result % 10, sep="")
