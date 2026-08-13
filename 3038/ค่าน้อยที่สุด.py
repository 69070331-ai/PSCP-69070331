"""ค่าน้อยที่สุด"""
a = int(input())
b = int(input())
c = int(input())

smallest = a

if b < smallest:
    smallest = b

if c < smallest:
    smallest = c

print(smallest)
