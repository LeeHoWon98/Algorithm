n1, n2 = input().split()
len_n = min(len(n1), len(n2))
result = ""
len_result = ""

if len(n1) > len(n2):
    len_n1 = len(n1) - len(n2)
    len_result = n1[:len_n1]
    for i in range(len_n):
        result += str(int(n1[len_n1+i]) + int(n2[i]))
    print(len_result+result)

elif len(n1) < len(n2):
    len_n2 = len(n2) - len(n1)
    len_result = n2[:len_n2]
    for i in range(len_n):
        result += str(int(n1[i]) + int(n2[len_n2+i]))
    print(len_result+result)

else:
    for i in range(len_n):
        result += str(int(n1[i]) + int(n2[i]))
    print(result)