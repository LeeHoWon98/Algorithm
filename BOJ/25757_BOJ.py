n1, s = input().split()
li = set()

for i in range(int(n1)):
    li.add(input())
    
if s == "Y":
    print(len(li))
    
elif s == "F":
    print(len(li)//2)

elif s == "O":
    print(len(li)//3)