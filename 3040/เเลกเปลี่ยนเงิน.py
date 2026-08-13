"""คำสั่งรับจำนวนเงินจากผู้ใช้เเละคำนวณจำนวนเหรียญที่ต้องใช้ในการจ่ายเงิน"""
money = int(input())

coin10 = money // 10
money = money - (coin10 * 10)

coin5 = money // 5
money = money - (coin5 * 5)

coin2 = money // 2
money = money - (coin2 * 2)

coin1 = money

print("10 =", coin10)
print("5 =", coin5)
print("2 =", coin2)
print("1 =", coin1)
