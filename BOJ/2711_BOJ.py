n = int(input())

for i in range(n):
    n1, word = input().split()
    word = list(word)
    word.pop(int(n1)-1)
    print("".join(word))