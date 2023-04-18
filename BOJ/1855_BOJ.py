n = int(input())
words = list(input())
words = [words[i:i+n] for i in range(0, len(words), n)]
result = []
result.append(words[0])

answer = ""

for j in range(1, len(words)):
    if j % 2 == 1:
        result.append(words[j][::-1])
    else:
        result.append(words[j])

for k in range(n):
    for l in range(len(result)):
        answer += result[l][k]

print(answer)