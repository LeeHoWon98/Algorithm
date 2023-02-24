def solution(n1, n2):
    re_conversion = ''

    while n1 > 0:
        n1, mod = divmod(n1, n2)
        re_conversion += str(mod)

    return re_conversion[::-1]
    
n1, n2 = map(int, input().split())

result = solution(n1, n2)
result = result.split("0")
result = " ".join(result).split()

print(solution(sum(map(int, result)), n2))