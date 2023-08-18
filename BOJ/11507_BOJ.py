d = {"P" : 13, "K" : 13, "H" : 13, "T" : 13}
s = input()
result = [s[i:i+3] for i in range(0, len(s)-2, 3)]

c = 0

for j in result:
    if result.count(j) == 2:
        print("GRESKA")
        c += 1
        break
    else:
        d[j[0]]-=1

if c == 0:
    print(*d.values())