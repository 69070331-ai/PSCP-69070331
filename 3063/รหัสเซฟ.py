"""รหัสเซฟ"""
ch = input()
num = int(input())

if ch == "H" and num == 4567:
    print("safe unlocked")
elif ch == "H":
    print("safe locked - change digit")
elif num == 4567:
    print("safe locked - change char")
else:
    print("safe locked")
  
