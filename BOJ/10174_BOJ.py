n = int(input())

for i in range(n):
    words = input().lower()
    if words == words[::-1]:
        print('Yes')
    else:
        print("No")