"""ค่าใหญ่ที่สุดในจำนวน N จำนวน"""
maximum = int(input())

count = 1

while count < 3:
    num = int(input())

    if num > maximum:
        maximum = num

    count += 1

print(maximum)
