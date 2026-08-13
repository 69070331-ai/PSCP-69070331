"""ฟิลเตอร์ AR TikTok"""
r, x, y = map(int, input().split())

distance = x**2 + y**2

if distance < r**2:
    print("IN")
elif distance == r**2:
    print("ON")
else:
    print("OUT")
