s, n = input().split()
s = s.lower()
n = int(n)

result = []
result.append(s[0])

for i in s[1:]:
    if result[-1] != i and i in "".join(result):
        continue

    else:
        result.append(i)

answer = result[0]

for j in result[1:]:
    if answer[-1] != j:
        answer += "]"
        answer += j
    else:
        answer += j

answer = answer.split("]")

for k in answer:
    if len(k) >= n:
        print(1, end="")
    else:
        print(0, end="")