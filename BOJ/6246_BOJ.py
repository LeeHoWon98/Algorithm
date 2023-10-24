n1, n2 = map(int, input().split())
li_bo = ["." for i in range(n1)]

for i in range(n2):
    slot1, slot2 = map(int, input().split())
    for j in range(slot1-1, len(li_bo), slot2):
        li_bo[j] = "1"

print("".join(li_bo).count("."))