n = int(input())
result = []

for i in range(n):
    S, I, D = input().split() 
    result.append([S, int(I), S[int(D)-1].upper()])

result.sort(key=lambda x:x[1])

for j in range(n):
    print(result[j][2], end="")