s = list(input())
n = int(input())

for i in range(n):
    n1, n2 = map(int, input().split())
    s[n1], s[n2] = s[n2], s[n1]

print("".join(s))