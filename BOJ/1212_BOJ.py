result = []
c = 1

for i in range(3):
    num = input()
    s = [num[0]]
    for i in range(1, len(num)):
        if num[i] == s:
            c += 1
        else:
            result.append(c)
            c = 1
    print(max(result))