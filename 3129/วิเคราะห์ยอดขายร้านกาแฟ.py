"วิเคราะห์ยอดขายร้านกาแฟ"
N = int(input())

sales = [int(input()) for _ in range(N)]

total = sum(sales)
maximum = max(sales)
minimum = min(sales)
average = total / N

print(total)
print(maximum)
print(minimum)
print(f"{average:.1f}")
