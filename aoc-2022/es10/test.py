import sys



user_input = list(map(lambda line: line.strip(),sys.stdin.readlines()))

cycle = 1
to_add = 0
index_input = 0
pending = False
value = 1

result = 0

arr_result = [0,value]

while index_input < len(user_input):
	if not pending:
		line = user_input[index_input]
		if line == 'noop':
			cycle += 1
			index_input += 1
		else:
			*garbage, to_add = line.split(' ')
			to_add = int(to_add)
			cycle += 1
			pending = True
	else:
		pending = False
		cycle += 1
		value += to_add
		index_input += 1
	if cycle in [20,60,100,140,180,220]:
		result += value*cycle
	arr_result.append(value)


matrix = [['.' for x in range(40)] for y in range(6)]
for i in range(1,len(arr_result[:241])):
	x = (i-1)%40
	y = (i-1)//40
	value = arr_result[i]
	if(abs(value - x) <= 1):
		matrix[y][x] = '#'
	else:
		matrix[y][x] = '.'

for line in matrix:
	print(' '.join(line))


print(result)