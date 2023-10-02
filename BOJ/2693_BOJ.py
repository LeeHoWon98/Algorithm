n = int(input())

for i in range(n):
    n = list(map(int, input().split()))
    n.sort()
    print(n[-3])