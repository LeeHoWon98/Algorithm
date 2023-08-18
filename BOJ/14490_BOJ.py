from math import gcd

s = input()
n1, n2 = s.split(":")

to_gcd = gcd(int(n1), int(n2))

print(str(int(n1)//to_gcd)+":"+str(int(n2)//to_gcd))