n = int(input())
arr = list(input().split())
c = 0

for i in range(len(arr)-1):
    if arr[i][-1] != arr[i+1][0]:
        c -= 1
    else:
        c += 1

if c < 0:
    print(0)
elif c >= 0:
    print(1)