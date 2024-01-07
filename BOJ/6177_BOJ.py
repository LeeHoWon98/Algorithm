import sys

n = int(sys.stdin.readline().rstrip())
num = []

for i in range(n):
  num.append(int(sys.stdin.readline().rstrip()))

num.sort()

print("{:.6f}".format(sum(num) / n))

if n % 2 == 0:
  if n > 2 :
    mid = n // 2
    print("{:.6f}".format((num[mid-1]+num[mid])/2))
  else:
    mid = n // 2
    print("{:.6f}".format((num[0]+num[1])/2))

else:
  mid = (n // 2)
  print("{:.6f}".format(num[mid]))