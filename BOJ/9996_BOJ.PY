n = int(input())
s1 = input()
result = s1.split('*')

for _ in range(n):
	s2 = input()
	if len(result[0])+len(result[1]) > len(s2):
		print("NE")
	else:
		if result[0] == s2[:len(result[0])] and result[1] == s2[-len(result[1]):]:
			print("DA")
		else:
			print("NE")