import sys

user_input = sys.stdin.readlines()

result = []
sum = 0
for line in user_input:
	try:
		sum += int(line)
	except:
		result += [sum]
		sum = 0

print(max(result))
