import sys
import copy


user_input = map(lambda line: line.strip(),sys.stdin.readlines())

monkeys = []

monkey_str = 'Monkey '
starting_str = 'Starting items: '
operation = 'Operation: new = old '
test = 'Test: divisible by '
if_true = 'If true: throw to monkey '
if_false = 'If false: throw to monkey '



for line in user_input:
	if monkey_str in line:
		assert int(line[len(monkey_str):-1]) == len(monkeys)
		monkey = {'index': len(monkeys)}
	elif starting_str in line:
		line = line[len(starting_str):]
		values = map(lambda i_str: int(i_str),line.split(', '))
		monkey['items'] = list(values)
	elif operation in line:
		line = line[len(operation):]
		op, value = line.split(' ')
		true_op = None
		if op == '+':
			true_op = int.__add__
		elif op == '*':
			true_op = int.__mul__
		else:
			raise Exception('bad operation')
		if value != 'old':
			value = int(value)
			fun = lambda true_op, value: lambda x: true_op(x,value)
			
		else:
			fun = lambda true_op, value: lambda x: true_op(x,x)
		monkey['operation'] = fun(true_op,value)
	elif test in line:
		line = line[len(test):]
		monkey['test'] = int(line)
	elif if_true in line:
		line = line[len(if_true)]
		monkey[str(True)] = int(line)
	elif if_false in line:
		line = line[len(if_false)]
		monkey[str(False)] = int(line)
	else:
		monkeys.append(monkey)
		assert not line
monkeys.append(monkey)



backupMonkeys = copy.deepcopy(monkeys)

#for part 2
modulo_magician = 1
for monkey in monkeys:
	if modulo_magician%monkey['test']:
		modulo_magician *= monkey['test']

def exercize(iterations,dividedBy = 1):
	for i in range(iterations):
		for monkey in monkeys:
			while len(monkey['items']):
				item = monkey['items'].pop(0)
				new_value = (monkey['operation'](item)//dividedBy)%modulo_magician
				tested = not (new_value % monkey['test'])
				next_monkey = monkey[str(tested)]
				activity_count[monkey['index']] += 1
				monkeys[next_monkey]['items'].append(new_value)
	

activity_count = [0 for x in monkeys]
exercize(20,3)
activity_count.sort(reverse=True)
print(activity_count[0]*activity_count[1])

monkeys = backupMonkeys
activity_count = [0 for x in monkeys]
exercize(10000)
activity_count.sort(reverse=True)
print(activity_count[0]*activity_count[1])

	
	