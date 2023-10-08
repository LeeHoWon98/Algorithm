s = input()
S = list(input().split())

result = ""

for i in s:
    if i in S:
        result += i.lower()
    else:
        result += i

print(result)