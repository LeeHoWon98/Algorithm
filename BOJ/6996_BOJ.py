n = int(input())

for i in range(n):
    s1, s2 = input().split()
    result1 = sorted(s1)
    result2 = sorted(s2)
    if result1 == result2:
        print(s1, "&", s2, "are anagrams.")
    else:
        print(s1, "&", s2, "are NOT anagrams.")