import sys
sys.setrecursionlimit(1000000)

def result(n):
    global sum
    if 1 > n:
        return sum
    sum += n
    result(n-1)
n = int(input())
sum = 0
result(n)
print(sum)