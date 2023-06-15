import sys
n1 = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
n2 = int(input())

li.sort()

s, e = 0, n1-1
c = 0

while s <= e:
    if li[s] + li[e] == n2:
        c += 1
        s += 1
    elif li[s] + li[e] < n2:
        s += 1
    else:
        e -= 1

print(c)