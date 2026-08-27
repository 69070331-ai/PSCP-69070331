"""วันเกิด"""
from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())

y2 = int(input())
m2 = int(input())
d2 = int(input())

day1 = date(y1, m1, d1)
day2 = date(y2, m2, d2)

diff = abs((day1 - day2).days)

if diff <= 7:
    print(0)
elif day1 < day2:
    print(1)
else:
    print(2)
  
