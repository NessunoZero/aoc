import sys
import string



user_input = sys.stdin.readlines()

def exercise(second_part = False):
	stacks = []
	line_stack_len = len(user_input[0]) -1
	stacks_count = (line_stack_len + 1)//4 + 1
	for i in range(stacks_count):
		stacks.append([])
	for line in user_input:
		tmp_line = line
		if 	'[' in tmp_line:
			i = 0
			k = 1
			while i < len(tmp_line):
				if tmp_line[i+1] in string.ascii_uppercase:
					stacks[k].append(tmp_line[i+1])
				i += 4
				k += 1
		elif 'move' in tmp_line:
			garbage, stuff = tmp_line.split('move ')
			how_many, stuff  = stuff.split(' from ')
			how_many = int(how_many)
			from_stack, to_stack = stuff.split(' to ')
			from_stack = int(from_stack)
			to_stack = int(to_stack)
			moving_stacks = stacks[from_stack][-how_many:]
			if not second_part:
				moving_stacks = moving_stacks[::-1]
			stacks[from_stack] = stacks[from_stack][:-how_many]
			stacks[to_stack] = stacks[to_stack] + moving_stacks

		elif not tmp_line.strip():
			for i in range(1,stacks_count):
				stacks[i] = stacks[i][::-1]

	print(stacks)
	result = ''
	for i in range(1,stacks_count):
		result += stacks[i][-1]
	print(result)

exercise()
exercise(True)