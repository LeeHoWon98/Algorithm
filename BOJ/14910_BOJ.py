n = list(map(int, input().split()))
result = n
new_result = sorted(n)

if result == new_result:
    print("Good")

elif result != new_result:
    print("Bad")