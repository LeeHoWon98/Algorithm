n1, low, high = map(int, input().split())
list_num = list(map(int, input().split()))

if high == 0:
    high = n1
    list_num.sort()
    print(sum(list_num[low:high])/len(list_num[low:high]))
else:
    list_num.sort()
    print(sum(list_num[low:-high])/len(list_num[low:-high]))