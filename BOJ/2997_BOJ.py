n = list(map(int, input().split()))
n.sort()
result = min(n[1]-n[0], n[2]-n[1])

for i in range(len(n)):
    temp = n[i]
    
    if temp+result not in n:
        print(temp+result)
        break