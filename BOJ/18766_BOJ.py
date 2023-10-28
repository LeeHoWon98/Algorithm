n = int(input())

for i in range(n):
    c = 0
    num = int(input())
    card1 = list(input().split())
    card2 = list(input().split())
    card1.sort()
    card2.sort()
    
    for j in range(num):
        if card1[j] != card2[j]:
            c += 1
    
    if c == 0:
        print("NOT CHEATER")
    else:
        print("CHEATER")