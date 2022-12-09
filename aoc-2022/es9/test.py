import sys



user_input = list(map(lambda line: line.strip(),sys.stdin.readlines()))

yet_visited_tail = set()
tail = 0, 0
head = 0, 0

def addTailToVisited():
	yet_visited_tail.add('_'.join(map(str,tail)))

def followUp(head, tail):
	x = head[0] - tail[0]
	y = head[1] - tail[1]
	if x == 0 or y == 0:
		if abs(x) <= 1 and abs(y) <= 1:
			return tail
		if x == 0:
			return tail[0],tail[1] + y//abs(y)
		else:
			return tail[0] + x//abs(x), tail[1]
	else:
		if abs(x) <= 1 and abs(y) <= 1:
			return tail
		return tail[0] + x//abs(x) , tail[1] + y//abs(y)

addTailToVisited()
for line in user_input:
	direction, steps = line.split(' ')
	steps = int(steps)
	for i in range(steps):
		if direction == 'U':
			head = head[0] + 1, head[1] 
		elif direction == 'D':
			head = head[0] - 1, head[1]
		elif direction == 'R':
			head = head[0], head[1] + 1
		elif direction == 'L':
			head = head[0], head[1] - 1
		tail = followUp(head, tail)
		addTailToVisited()

head = 0,0
tails = list(map(lambda i: (0,0),range(9)))
yet_visited_tail_9 = set()

def addTail9ToVisited():
	yet_visited_tail_9.add('_'.join(map(str,tails[8])))

addTail9ToVisited()
for line in user_input:
	direction, steps = line.split(' ')
	steps = int(steps)
	for i in range(steps):
		if direction == 'U':
			head = head[0] + 1, head[1] 
		elif direction == 'D':
			head = head[0] - 1, head[1]
		elif direction == 'R':
			head = head[0], head[1] + 1
		elif direction == 'L':
			head = head[0], head[1] - 1
		tails[0] = followUp(head, tails[0])
		for j in range(8):
			tails[j+1] = followUp(tails[j],tails[j+1])
		addTail9ToVisited()

print(len(yet_visited_tail))
print(len(yet_visited_tail_9))