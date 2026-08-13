"""ค่าเล็กที่สุดในจำนวน N จำนวน"""
N = int(input())

minimum = int(input())

count = 1

while count < N:
    num = int(input())

    if num < minimum:
        minimum = num

    count += 1

print(minimum)
