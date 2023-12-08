n1 = input()
n2 = input()

if len(n1) > len(n2):
    n2 = '0'*(len(n1)-len(n2)) + n2
else:
    n1 = '0'*(len(n2)-len(n1)) + n1

result_n1 = ""
result_n2 = ""

for i in range(len(n1)):
    if int(n1[i]) > int(n2[i]):
        result_n1 += n1[i]
    elif int(n2[i]) > int(n1[i]):
        result_n2 += n2[i]
    else:
       result_n1 += n1[i]
       result_n2 += n2[i] 

if len(result_n1) == 0:
    print('YODA')
    print(int(result_n2))
elif len(result_n2) == 0:
    print(int(result_n1))
    print('YODA')
else:
    print(int(result_n1))
    print(int(result_n2))