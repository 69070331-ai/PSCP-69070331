"ตั๋วหนังสุดป่วน"
seats = int(input())

while seats > 0:
    try:
        age, tickets = map(int, input().split())
    except EOFError:
        break

    if age < 15:
        print(-1)

    elif tickets > seats:
        print(-2)

    else:
        if age <= 22:
            PRICE = 120
        elif age >= 60:
            PRICE = 75
        else:
            PRICE = 150

        total = PRICE * tickets
        seats -= tickets

        print(total, seats)
