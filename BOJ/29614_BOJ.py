s = list(input())
n = []
result = []

for i in range(len(s)-1):
    if s[i+1] == "+":
        n.append(s[i]+s[i+1])
    else:
        n.append(s[i])

if s[-1] != "+":
    n.append(s[-1])
else:
    n.append(n[-1]+s[-1])

for j in n:
    if j == "A+":
        result.append(4.5)
    elif j == "A":
        result.append(4.0)
    elif j == "B+":
        result.append(3.5)
    elif j == "B":
        result.append(3.0)
    elif j == "C+":
        result.append(2.5)
    elif j == "C":
        result.append(2.0)
    elif j == "D+":
        result.append(1.5)
    elif j == "D":
        result.append(1.0)
    elif j == "F":
        result.append(0.0)

print("{:.4f}".format(sum(result)/len(result)))