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
result.sort(reverse=True)
print(result[0])
print(result[1])
print(result[2])
print(result[0]+result[1]+result[2])
