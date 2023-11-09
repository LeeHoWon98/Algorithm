n = int(input())
result = [i for i in range(1, n+1)]
answer = []

while len(result) != 1:
    answer.append(result.pop(0))
    result.append(result.pop(0))
 
print(*answer,*result)