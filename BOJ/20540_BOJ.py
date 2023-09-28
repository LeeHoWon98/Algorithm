s = input()
result = []

for i in s:
    if i == "E":
        result.append("I")
    elif i == "I":
        result.append("E")
    elif i == "N":
        result.append("S")
    elif i == "S":
        result.append("N")
    elif i == "T":
        result.append("F")
    elif i == "F":
        result.append("T")
    elif i == "J":
        result.append("P")
    elif i == "P":
        result.append("J")

print("".join(result))