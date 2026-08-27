"ตรวจสอบปีอธิกสุรทิน"
n = int(input())

if n < 1582:
    if not n % 4 :
        print("yes")
    else:
        print("no")
else:
    if not n % 400:
        print("yes")
    elif not n % 100:
        print("no")
    elif not n % 4:
        print("yes")
    else:
        print("no")
      
