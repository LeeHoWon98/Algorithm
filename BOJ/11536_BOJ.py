n = int(input())
name = []
new_name = []

for i in range(n):
    s = input()
    name.append(s)
    new_name.append(s)

name.sort()

if name == new_name:
    print("INCREASING")

elif name == new_name[::-1]:
    print("DECREASING")

else:
    print("NEITHER")