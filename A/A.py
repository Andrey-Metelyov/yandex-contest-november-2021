J = set(input())
S = input()

count = 0
for s in S:
	if s in J:
		count += 1
print(count)
