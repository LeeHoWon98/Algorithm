import sys
input = sys.stdin.readline

n1, n2 = map(int, input().split())

d = {}

for i in range(n1):
    s1, s2 = input().split()
    d[s1] = s2

for j in range(n2):
    result = input().rstrip()
    print(d[result])