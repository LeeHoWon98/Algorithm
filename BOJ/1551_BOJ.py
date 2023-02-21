n1, n2 = map(int, input().split())
result = list(map(int, input().split(',')))

for i in range(n2):
    result = [result[i+1]-result[i]for i in range(len(result)-1)]

print(*result,sep=",")