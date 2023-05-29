N = int(input())
n_set = set(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

print(*[1 if i in n_set else 0 for i in m_list], sep="\n")