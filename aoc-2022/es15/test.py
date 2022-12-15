import sys

user_input = map(lambda line: line.strip(),sys.stdin.readlines())

sensors = []
for line in user_input:
  line = line[len('Sensor at x='):]
  line = line.split(': closest beacon is at x=')
  s, b = line
  s = tuple(map(int,s.split(', y=')))
  b = tuple(map(int,b.split(', y=')))
  d = abs(s[0] - b[0]) + abs(s[1] - b[1])
  sensors.append((s,b,d))


def check_a_line(y):
  beacons = set()
  checked = set()
  
  for s,b,d in sensors:
    if b[1] == y:
      beacons.add(b[0])
    l_d = abs(y-s[1])
    free_d = d - l_d
    if free_d >= 0:
      for i in range(-free_d,free_d + 1):
        checked.add(i+s[0])
  counter = 0
  
  for index in checked:
    if not index in beacons:
      counter += 1
  print(y,': ',counter)

check_a_line(10)
check_a_line(2000000)

def check_a_line_part_2(y):
  checked_intervals = []

  for s,b,d in sensors:
    if b[1] == y:
      checked_intervals.append((b[0],0))
    if s[1] == y:
      checked_intervals.append((s[0],0))
    l_d = abs(y-s[1])
    free_d = d - l_d
    if free_d >= 0:
      checked_intervals.append((s[0]-free_d,2*free_d))
  
  checked_intervals.sort(key=lambda x: x[0])
  result_intervals = []
  c_i_s, c_i_l = None, None
  for s,l in checked_intervals:
    if not c_i_s:
      c_i_s, c_i_l = s,l
    elif s > c_i_s + c_i_l + 1:
      result_intervals.append((c_i_s,c_i_l))
      c_i_s, c_i_l = None, None
    else:
      new_l = s + l - c_i_s
      c_i_l = max(c_i_l,new_l)
  if c_i_s:
    result_intervals.append((c_i_s,c_i_l))
  return result_intervals


valid_range_t = 4000000 + 1
valid_range = valid_range_t
beacon = None


solution = None
resolved = False
for y in range(valid_range):
  checked_intervals = check_a_line_part_2(y)
  for interval in checked_intervals:
    solution = interval[0] - 1, y
    if solution[0] >= 0 and solution[0] < valid_range:
      resolved = True
      break
  if not resolved:
    solution = None
  else:
    break
    

print(solution[0]*(valid_range-1)+solution[1])
