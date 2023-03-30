import collections

s1 = input()
s1 = s1.lower()

counts1 = collections.Counter(s1)

counts = sorted(counts1.values(), reverse = True)

if len(counts) != 1:
    if counts[0] == counts[1]:
        print("?")
    else:
        print(str(counts1.most_common(1)[0][0]).upper())
else:
    print(str(counts1.most_common(1)[0][0]).upper())