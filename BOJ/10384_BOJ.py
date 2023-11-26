n = int(input())
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']
for i in range(n):
    d = {}
    s = input()
    for j in s:
        if j.isalpha():
            if j.lower() in d:
                d[j.lower()] += 1
            else:
                d[j.lower()] = 1
    d = dict(sorted(d.items(), key=lambda x:x[0]))
    result = list(d.keys())
    
    if result == alpa:
        if min(d.values()) == 1:
            print("Case {}: Pangram!".format(i+1))
        elif min(d.values()) == 2:
            print("Case {}: Double pangram!!".format(i+1))
        elif min(d.values()) == 3:
             print("Case {}: Triple pangram!!!".format(i+1))

    else:
        print("Case {}: Not a pangram".format(i+1))