n = 2
output = 0
inputs = [1, 4, 3, 2]

result = []

inputs.sort()

for i in inputs:
    result.append(i)
    if len(result) == 2:
        output += min(result)
        result.clear()

print(output)