n = input()
n = n.split("->")

if n == n[::-1]:
    print("true")

elif n != n[::-1]:
    print("false")