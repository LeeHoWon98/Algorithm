import sys

while True:
    try:
        d = dict()
        result = []
        words1 = set(sys.stdin.readline().rstrip())
        words2 = set(sys.stdin.readline().rstrip())
        
        for i in words1:
            d[i] = 1
            
        for j in words2:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
                
        for k, v in d.items():
            if v == 2:
                result.append(k)
            else:
                continue
        result.sort()
        print("".join(result))
    except:
        break