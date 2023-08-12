d = {'0' : "zero", '1' : "one", '2' : "two", '3' : "three", '4' : "four", '5' : "five", '6' : "six", '7' : "seven", 
     '8' : "eight", '9' : "nine"}

n1, n2 = map(int, input().split())

result = []

for i in range(n1, n2+1):
    s = " ".join([d[j] for j in str(i)])
    result.append([i, s])

result.sort(key=lambda x:x[1])

for j in range(len(result)):
    if j % 10 == 0 and j != 0:
        print()
    print(result[j][0], end = " ")