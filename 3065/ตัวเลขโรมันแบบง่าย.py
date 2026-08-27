"""factorial"""
n = int(input())

roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

if n < 0:
    print("Error : Please input positive number")
elif not n or n > 9:
    print("Error : Out of range")
else:
    print(roman[n - 1])
  
