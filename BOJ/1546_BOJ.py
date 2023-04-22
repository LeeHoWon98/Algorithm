n = int(input())
point = list(map(int, input().split()))
m_point = max(point)

sum = 0

for i in point:
    sum += i/m_point*100

print("%.2f"%(sum/n))