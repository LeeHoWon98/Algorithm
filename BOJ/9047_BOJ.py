n = int(input())

for i in range(n):
    c = 0
    n1 = input()

    while n1 != "6174" :
        min_n = int("".join(sorted(n1)))
        max_n = int("".join(sorted(n1, reverse=True)))
        n1 = str(max_n - min_n)

        if len(n1) < 4:
            s = ""
            for i in range(4 - len(n1)):
                s += "0"
            n1 = s + n1

        c += 1
    
    print(c)