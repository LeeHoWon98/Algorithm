import sys

n = int(sys.stdin.readline())
st = []

for i in range(n):
    s = sys.stdin.readline().split()
    
    if s[0] == 'push':
        st.append(int(s[1]))
        
    elif s[0] == 'pop':
        if len(st) != 0:
            print(st.pop())
        else:
            print(-1)
        
    elif s[0] == 'size':
        print(len(st))
        
    elif s[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
            
    elif s[0] == 'top':
        if len(st) != 0:
            print(st[-1])
        else:
            print(-1)