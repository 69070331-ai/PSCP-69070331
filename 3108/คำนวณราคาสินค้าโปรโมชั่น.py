"คำนวณราคาสินค้าโปรโมชั่น"
a, b, c = input() .split()

a = int(a)
b = int(b)
c = int(c)

total = a * 25 + b * 40 + c * 55

if a + b + c >= 3:
    total = int(total-(total * 10 / 100))

print(total)
