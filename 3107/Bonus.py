"Bonus"
position, year, salary = input().split()

year = int(year)
salary = int(salary)

if position == "M":
    BONUS = 1500
elif position == "B":
    BONUS = 1000
else:
    BONUS = 500

if year <= 5:
    if position == "M":
        PERCENT = 6
    elif position == "B":
        PERCENT = 5
    else:
        PERCENT = 4

elif year <= 10:
    if position == "M":
        PERCENT = 8
    elif position == "B":
        PERCENT = 6
    else:
        PERCENT = 5

else:
    if position == "M":
        PERCENT = 10
    elif position == "B":
        PERCENT = 7
    else:
        PERCENT = 6

total = BONUS + (salary * PERCENT / 100)

print(int(total))
