s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = input()
    
s_max = max(len(s1), len(s2), len(s3), len(s4), len(s5))
result = [[s1], [s2], [s3], [s4], [s5]]

for i in range(len(result)):
    if len(result[i]) < s_max:
        s = "".join(result[i])
        new_s = s.ljust(6)
        result[i] = new_s

result_s = ""

for j in range(s_max):
    for k in range(len(result)):
        result_s += result[k][j]

result_s = result_s.replace(" ", "")

print(result_s)