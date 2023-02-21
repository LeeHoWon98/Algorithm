n = int(input())
result = {}
s = ""

for i in range(n):
    w, word = input().split()
    result[word] = w

words = input()
n1, n2 = map(int,input().split())

for j in words:
    s += result[j]
    
print(s[n1-1:n2])