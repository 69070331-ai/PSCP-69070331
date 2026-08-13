"""กระดาษห่อของขวัญ"""
r, h, glue = map(float, input().split())

width = 2 * r + h
length = 2 * 3.14 * r + glue

print(f"{width:.2f} {length:.2f}")
