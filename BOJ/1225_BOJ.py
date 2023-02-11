n = int(input())
s = [str(i) for i in range(1, n+1)]
s1 = "".join(s)
print(s1.find(str(n))+1)