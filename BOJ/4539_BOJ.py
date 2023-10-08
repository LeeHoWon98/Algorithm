n = int(input())

for i in range(n):
    n1 = list(input())
    result = ""
    for j in range(1, len(n1)):
        if int(n1[-j]) >= 5:
            n1[-j+1] = str(int(n1[j-1])+1)
        n1[j] = "0"
    print("".join(n1))