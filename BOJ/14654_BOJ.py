n = int(input())
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))

c1, c2 = 0, 0
max_streak = 0

for i in range(n):
    if n1[i] == 1:
        if n2[i] == 2:
            c1 = 0
            c2 += 1
        elif n2[i] == 3:
            c1 += 1
            c2 = 0
        elif n1[i] == n2[i]:
            if c1 >= 1:
                c1 = 0
                c2 += 1
            elif c2 >= 1:
                c1 += 1
                c2 = 0

    elif n1[i] == 2:
        if n2[i] == 1:
            c1 += 1
            c2 = 0
        elif n2[i] == 3:
            c1 = 0
            c2 += 1
        elif n1[i] == n2[i]:
            if c1 >= 1:
                c1 = 0
                c2 += 1
            elif c2 >= 1:
                c1 += 1
                c2 = 0

    elif n1[i] == 3:
        if n2[i] == 1:
            c1 = 0
            c2 += 1
        elif n2[i] == 2:
            c1 += 1
            c2 = 0
        elif n1[i] == n2[i]:
            if c1 >= 1:
                c1 = 0
                c2 += 1
            elif c2 >= 1:
                c1 += 1
                c2 = 0

    max_streak = max(max_streak, c1, c2)

print(max_streak)