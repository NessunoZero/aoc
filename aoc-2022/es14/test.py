import sys

user_input = map(lambda line: line.strip(),sys.stdin.readlines())


segments = []
for line in user_input:
	line = line.split(' -> ')
	segments.append(list(map(lambda l: tuple(map(int,l)),map(lambda pair:pair.split(','),line))))

max_x = max(segments[0],key=lambda x: x[0])[0]
min_x = min(segments[0],key=lambda x: x[0])[0]
max_y = max(segments[0],key=lambda x: x[1])[1]
min_y = min(segments[0],key=lambda x: x[1])[1]
for row in segments:
	max_x = max(max(row,key=lambda x: x[0])[0],max_x)
	min_x = min(min(row,key=lambda x: x[0])[0],min_x)
	max_y = max(max(row,key=lambda x: x[1])[1],max_y)
	min_y = min(min(row,key=lambda x: x[1])[1],min_y)


h = max_y + 1
w = max_x-min_x + 1
matrix = [['.' for j in range(w)] for i in range(h)]

def draw(start,end):
	first, last = None, None
	if start[0] == end[0]:
		first = min(start[1], end[1])
		last = max(start[1],end[1])
		for i in range(last - first + 1):
			matrix[first + i][start[0] - min_x] = '#'
	if start[1] == end[1]:
		first = min(start[0], end[0])
		last = max(start[0],end[0])
		for i in range(last - first + 1):
			matrix[start[1]][first + i - min_x] = '#'

last = None
for seg in segments:
	last = None
	for pair in seg:
		if last is None:
			last = pair
		else:
			draw(last,pair)
			last = pair



def check_pos(pos):
	x, y = pos
	if y < 0 or y >= w or x >= h:
		return None
	elif matrix[x][y] != '.':
		return False
	return True

def insert_next_pos(pos):
	check = check_pos(pos)
	if check:
		return insert_sand(pos)
	elif check is None:
		return None
	else:
		return False

def insert_sand(pos):
	i = pos[0]
	j = pos[1]
	nexts = [(i+1,j),(i+1, j-1), (i+1, j+1)]
	for next in nexts:
		check = insert_next_pos(next)
		if check is None:
			return None
		elif check:
			return True
		else:
			pass
	matrix[i][j] = 'o'
	return True

inserted_sand = True
counter = 0

while inserted_sand:
	pos = 0, 500 - min_x
	if check_pos(pos):
		inserted_sand = insert_sand(pos)
		if inserted_sand:
			counter += 1
	else:
		break


print(counter)
