"Conan"
text = input()
k = int(input())

result = ""

for ch in text:
    result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))

print(result)
