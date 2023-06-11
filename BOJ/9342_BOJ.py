import re

n = int(input())
result = re.compile('[A-F]?A+F+C+[A-F]?')

for i in range(n):
    s = input()
    if result.fullmatch(s):
        print('Infected!')
    else:
        print('Good')