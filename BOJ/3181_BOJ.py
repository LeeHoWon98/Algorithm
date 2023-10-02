s = input()
s = s.split()

new_s = ""

result = ['i', 'pa', 'te', 'ni', 'niti', 'a',
          'ali', 'nego', 'no', 'ili']

for i in result:
    if i in s:
        if s[0] == i:
            pass
        else:
            s.remove(i)

for j in s:
    new_s += j[0].upper()

print(new_s)