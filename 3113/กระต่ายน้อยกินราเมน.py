"การเพิ่ม/ลด"
size, ramen_type = input().split()

if size == "S" and ramen_type == "R":
    price = 60
elif size == "S" and ramen_type == "T":
    price = 80
elif size == "M" and ramen_type == "R":
    price = 80
elif size == "M" and ramen_type == "T":
    price = 100
elif size == "L" and ramen_type == "R":
    price = 100
else:
    price = 120
  
