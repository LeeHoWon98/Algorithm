li_n, n = map(int, input().split())
li = list(map(int, input().split()))

win = sum(li[:n])
result = win

for i in range(n, len(li)):
    win += li[i] - li[i - n]
    result = max(result, win)
    
print(result)