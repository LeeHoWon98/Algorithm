s1 = input()
s2 = input()

s1_len = len(s1)
s2_len = len(s2)

if s1*s2_len == s2*s1_len:
    print(1)
else:
    print(0)