"Teaching schedule"
N = int(input())
A = int(input())

total = N * A

if  not total:
    print("No teaching")
else:
    hours = total // 60
    minutes = total % 60

    if not hours:
        print(minutes, "minute")
    elif not minutes:
        print(hours, "hours")
    else:
        print(hours, "hours", minutes, "minute")
      
