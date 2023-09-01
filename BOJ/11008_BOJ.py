n = int(input())

for i in range(n):
    s, s1 = input().split()
    s = s.replace(s1, "1")
    print(len(s))