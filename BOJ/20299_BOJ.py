import sys
input = sys.stdin.readline

list_om = ["black", "brown", "red", "orange", "yellow", "green", "blue",
           "violet", "grey", "white"]

color1 = input().rstrip()
color2 = input().rstrip()
color3 = input().rstrip()

result = int(str(list_om.index(color1)) + str(list_om.index(color2))) * int(10 ** int(str(list_om.index(color3))))

print(result)