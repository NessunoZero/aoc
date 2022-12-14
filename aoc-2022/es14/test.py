import sys
from copy import deepcopy

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
matrix = set()

def get_label(x,y):
  return f'{x}_{y}'

def draw(start,end):
	first, last = None, None
	if start[0] == end[0]:
		first = min(start[1], end[1])
		last = max(start[1],end[1])
		for i in range(last - first + 1):
			matrix.add(get_label(first + i,start[0] - min_x))
	if start[1] == end[1]:
		first = min(start[0], end[0])
		last = max(start[0],end[0])
		for i in range(last - first + 1):
			matrix.add(get_label(start[1],first + i - min_x))

last = None
for seg in segments:
	last = None
	for pair in seg:
		if last is None:
			last = pair
		else:
			draw(last,pair)
			last = pair

class controller():
  def __init__(self,index_rule,max_index = None):
    self.index_rule = index_rule
    self.max_index = max_index
    self.stones = deepcopy(matrix)
    self.sand = set()

  def check_pos(self,pos):
    x, y = pos
    label = get_label(x,y)
    if self.max_index and self.max_index == x:
      return False
    if self.index_rule(x,y):
      return None
    elif label in self.stones or label in self.sand:
      return False
    return True
  
  def put_sand(self,pos):
    self.sand.add(get_label(*pos))

def index_rule_part1(x,y):
  return y < 0 or y >= w or x >= h

def index_rule_part2(*args):
  return False

max_index_part1 = None
max_index_part2 = h+1

def exercize(index_rule,max_index):
  checker = controller(index_rule,max_index)
  count = 0
  sand_placed = True

  falling_sand = True
  
  while sand_placed:
    sand_placed = False
    pos = (0,500-min_x)
    falling_sand = True
    while falling_sand:
      falling_sand = False
      if checker.check_pos(pos):
        x,y = pos
        aNone = False
        aTrue = False
        for next in map(lambda npos: (npos,checker.check_pos(npos)),[(x+1,y),(x+1, y-1), (x+1, y+1)]):
          if next[1] is None:
            aNone = True
            break
          elif next[1] is True:
            pos = next[0]
            aTrue = True
            break
        if aNone:
          sand_placed = False
          break
        elif aTrue:
          falling_sand = True
        else:
          checker.put_sand(pos)
          count += 1
          sand_placed = True
          break

  print(count)

exercize(index_rule_part1,max_index_part1)
exercize(index_rule_part2,max_index_part2)