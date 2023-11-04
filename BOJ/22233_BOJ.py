import sys

n1, n2 = map(int, sys.stdin.readline().split())
d = {}
c = 0

for i in range(n1):
    word = sys.stdin.readline().rstrip()
    d[word] = 1
    c += 1

for j in range(n2):
    word = sys.stdin.readline().rstrip()
    if "," in word:
        li_word = word.split(",")
        for k in li_word:
            if k in d:
                c -= 1
                del d[k]
            else:
                continue
    else:
        if word in d:
            c -= 1
            del d[word]

    print(c)