n = int(input())

for i in range(n):
    num = list(map(int,input()))
    s = set(num)
    print(len(s))