while True:
    s = input().lower()
    s1 = s[0]
    s2 = s[1:]
    if s == "#":
        break
    else:
        print(s1, s2.count(s1))