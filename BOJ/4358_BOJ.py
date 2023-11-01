import sys

d = {}
c = 0

while 1:
    wood = sys.stdin.readline().rstrip()
    if wood == "":
        break
    if wood in d:
        d[wood] += 1
    else:
        d[wood] = 1
    c += 1

d = dict(sorted(d.items()))

for k, v in d.items():
    print("{0} {1:.4f}".format(k, (v/c)*100))