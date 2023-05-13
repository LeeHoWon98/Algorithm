result = [[], [], []]

n = int(input())

sum = []

for i in range(n):
    score1, score2, score3 = map(int, input().split())
    result[0].append(score1)
    result[1].append(score2)
    result[2].append(score3)
    
for j in range(n):
    answer = 0
    for k in range(3):
        if result[k].count(result[k][j]) == 1:
            answer += result[k][j]
            
    sum.append(answer)
    
for l in sum:
    print(l)