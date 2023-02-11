s = input()

if 'A' in s:
    s = s.replace('B', 'A')
    s = s.replace('C', 'A')
    s = s.replace('D', 'A')
    s = s.replace('F', 'A')
elif 'A' not in s and 'B' in s:
    s = s.replace('C', 'B')
    s = s.replace('D', 'B')
    s = s.replace('F', 'B')
elif 'A' not in s and 'B' not in s and 'C' in s:
    s = s.replace('D', 'C')
    s = s.replace('F', 'C')
elif 'A' not in s and 'B' not in s and 'C' not in s:
    s = "A"*len(s)

print(s)