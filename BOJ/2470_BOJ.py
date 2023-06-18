n = int(input())
li = list(map(int, input().split()))
li.sort()

s,e = 0, len(li)-1

point = abs(li[s]+li[e])
result = [li[s], li[e]]

while s < e:
    if abs(li[s]+li[e]) < point:
        point = abs(li[s]+li[e])
        result = [li[s], li[e]]
        if point == 0:
            break
    if li[s]+li[e] < 0:
        s += 1
    else:
        e -= 1
        
print(result[0], result[1])