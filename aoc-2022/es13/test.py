import sys
from ast import literal_eval

user_input = map(lambda line: line.strip(),sys.stdin.readlines())

first, second = None, None
pairs = []

for line in user_input:
	if first is None:
		first = literal_eval(line)
	elif second is None:
		second = literal_eval(line)
	else:
		pairs.append((first,second))
		first, second = None, None

pairs.append((first,second))

def check_order(first,second):
	if type(first) == type(second) and type(first) == int:
		if first == second:
			return None
		else:
			return first < second
	else:
		if type(first) != type(second):
			if type(first) == int:
				first = [first]
			else:
				second = [second]
		if type(first) == type(second) and type(first == list):
			n_f = len(first)
			n_s = len(second)
			for i in range(max(n_f,n_s)):
				if i >= n_f:
					return True
				elif i >= n_s:
					return False
				else:
					sub_check = check_order(first[i],second[i])
					if not sub_check is None:
						return sub_check
			return None

result = 0
for index in range(len(pairs)):
	if check_order(*pairs[index]):
		result += index + 1

print(result)

to_sort = [x[0] for x in pairs] + [x[1] for x in pairs] + [[[2]] , [[6]]]

for i in range(len(to_sort)):
	for j in range(len(to_sort)-1):
		if check_order(to_sort[j],to_sort[j+1]) is False:
			to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]


print((to_sort.index([[2]]) + 1)*(to_sort.index([[6]])+1))
