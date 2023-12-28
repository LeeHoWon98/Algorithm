gemi = list(map(int, input().split()))
start = list(map(int, input().split()))

total_gemi = 0
total_start = 0

flag = False

for i in range(9):
    total_gemi += gemi[i]

    if total_gemi > total_start:
        flag = True

    total_start += start[i]

if total_gemi < total_start and flag == True:
    print('Yes')

else:
    print('No')