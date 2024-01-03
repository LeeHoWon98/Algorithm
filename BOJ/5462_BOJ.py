n,t,p = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)] 
r = [[0,0] for _ in range(n)]    # [점수, 푼 문제 수]
s = [0]*t               # 각 문제를 몇 명이 못 풀었는지에 대한 리스트
 
for i in range(n):                # 문제의 점수가 될 2중 for문
    for j in range(t):
        if a[i][j] == 0:   
            s[j]+=1
 
for i in range(n):                  # ID별 점수와 푼 문제를 구할 2중 for문
    for j in range(t):
        if a[i][j] == 1:
            r[i][0]+=s[j]
            r[i][1]+=1
 
k1, k2 = r[p-1][0], r[p-1][1]      # 필립의 점수와 푼 문제 수
c=1                                   # 필립의 등수가 될 변수
for i in range(n):
    if r[i][0] > k1:                  # 조건 1
        c+=1
    elif r[i][0] == k1 and r[i][1] > k2:     # 조건 2
        c+=1
    elif r[i][0] == k1 and r[i][1] == k2 and i+1 < p:   # 조건 3
        c+=1
print(k1,c)