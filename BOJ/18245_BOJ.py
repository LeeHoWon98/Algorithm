line = 2

while 1:
    s = input()
    
    if s == "Was it a cat I saw?":
        break

    else:
        for i in range(0, len(s), line):
            print(s[i], end = '')
        print()

        line += 1