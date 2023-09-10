import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().split())

d = {}

for i in s:
    if i[-6:] == "Cheese":
        d[i] = 1

if sum(d.values()) >= 4:
    print("yummy")
else:
    print("sad")