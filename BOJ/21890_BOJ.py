n = int(input())
c = 0

for i in range(n):
    file = input()
    if file.count(".") == 1:
        file1, file2 = file.split(".")
        if len(file1) <= 8 and len(file1) != 0 and\
            len(file2) <= 3 and len(file2) != 0:
            c += 1

print(c)