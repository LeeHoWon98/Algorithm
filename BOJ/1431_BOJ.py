import sys

def sum_word(x):
    sum = 0
    for i in x:
        if i.isdigit():
            sum += int(i)
    return sum

n = int(sys.stdin.readline())

result = []

for i in range(n):
    s = sys.stdin.readline().rstrip()
    result.append(s)

result.sort(key=lambda x:(len(x), sum_word(x), x))

for j in result:
    print(j)