target = int(input())
num_list = list(map(int, input().split()))

left, right = 0, len(num_list)-1

while left != right:
    if num_list[left] + num_list[right] == target:
        print(num_list[left], num_list[right])
        break
    
    elif num_list[left] + num_list[right] > target:
        right -= 1

    elif num_list[left] + num_list[right] < target:
        left += 1