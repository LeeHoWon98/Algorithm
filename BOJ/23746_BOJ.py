n = int(input())
d = {}

for i in range(n):
    low_word, up_word = input().split()
    d[up_word] = low_word

word = input()
n1, n2 = map(int, input().split())
result = ""

for j in word:
    result += d[j]

print(result[n1-1:n2])