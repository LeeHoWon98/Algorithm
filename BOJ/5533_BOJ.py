n = int(input())
p1 = []
p2 = []
p3 = []
result1 = []
result2 = []
result3 = []

for i in range(n):
    s1, s2, s3 = map(int, input().split())
    p1.append(s1)
    p2.append(s2)
    p3.append(s3)

for k in range(n):
    if p1.count(p1[k]) >= 2:
        result1.append(0)
    if p2.count(p2[k]) >= 2:
        result2.append(0)
    if p3.count(p3[k]) >= 2:
        result3.append(0)
    if p1.count(p1[k]) == 1:
        result1.append(p1[k])
    if p2.count(p2[k]) == 1:
        result2.append(p2[k])
    if p3.count(p3[k]) == 1:
        result3.append(p3[k])

answer = [result1[i] + result2[i] + result3[i] for i in range(len(result1))]

for l in answer:
    print(l)