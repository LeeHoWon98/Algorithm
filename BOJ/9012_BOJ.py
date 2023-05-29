import sys

n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline()
    result = 0
    for j in a:
        
        if j == '(':
            result += 1
            
        elif j == ')':
            result -= 1
            
        if result < 0:
            print("NO")
            break
        
    if result == 0:
        print("YES")
        
    elif result > 0:
        print("NO")