n1, n2 = input().split()
ls1 = list(input().split())
ls2 = list(input().split())

diff_ls = list(set(ls1) ^ set(ls2))

print(len(diff_ls))