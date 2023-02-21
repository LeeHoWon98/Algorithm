n1, n2 = input().split()

n3 = int(n1[::-1]) + int(n2[::-1])
n3 = str(n3)

print(int(n3[::-1]))