n = int(input())

for i in range(n):
    s1, s2 = input().split()
    s1 = s1.replace(s2, "1")
    print(len(s1))