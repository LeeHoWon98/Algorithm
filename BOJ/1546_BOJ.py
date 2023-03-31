n = int(input())
m = list(map(int, input().split()))
new_max = max(m)

for i in range(n):
    m[i] = m[i]/new_max*100

print("%.2f" %(sum(m)/ n))