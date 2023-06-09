import sys

n = int(sys.stdin.readline())
d = dict()

for i in range(n):
    s1, s2 = sys.stdin.readline().split('.')
    if s2 in d:
        d[s2] += 1
    else:
        d[s2] = 1
        
d = sorted(d.items())

for k, v in d:
    print(k.rstrip(), v)