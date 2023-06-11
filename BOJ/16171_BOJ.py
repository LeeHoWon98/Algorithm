s1 = input()
s2 = input()
new_s = ""

for i in s1:
    if i.isdigit():
        continue
    else:
        new_s += i
        
if s2 in new_s:
    print(1)
else:
    print(0)