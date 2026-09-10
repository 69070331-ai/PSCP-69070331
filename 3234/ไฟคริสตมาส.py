"ไฟคริสตมาส"
color, n = input().split()
n = int(n)

colors = ["Red", "Green", "Blue"]

if color == "R":
    START= 0
elif color == "G":
    START = 1
else:
    START = 2

for i in range(n):
    print(colors[(START + i) % 3], end=" ")
