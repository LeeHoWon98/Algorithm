li_n = int(input())
att = int(input())
li = list(map(int, input().split()))
li.sort()

s, e = 0, len(li)-1
c = 0

while s < e:
    if li[s]+li[e] == att:
        c += 1
        s += 1
    elif li[s]+li[e] < att:
        s += 1
    else:
        e -= 1
        
print(c)