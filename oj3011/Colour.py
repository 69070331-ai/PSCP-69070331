"""Colors"""
color1 = input()
color2 = input()

if color1 not in ["Red", "Yellow", "Blue"] or color2 not in ["Red", "Yellow", "Blue"]:
    print("Error")
else:
    colors = {color1, color2}

    if colors == {"Red", "Yellow"}:
        print("Orange")
    elif colors == {"Red", "Blue"}:
        print("Violet")
    elif colors == {"Yellow", "Blue"}:
        print("Green")
    elif color1 == color2:
        print(color1)
        