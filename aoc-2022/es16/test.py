import sys
from copy import deepcopy

user_input = map(lambda line: line.strip(),sys.stdin.readlines())

valves = {}
indexes = {}

index = 0
for line in user_input:
  data = line.replace('Valve ','-').replace(' has flow rate=','-').replace('; tunnels lead to valves ','-').replace('; tunnel leads to valve ','-').split('-')
  valves[data[1]] = (int(data[2]),list(data[3].split(', ')))
  indexes[data[1]] = index
  index += 1
current = 'AA'


def calculate_distances():
  valves_distances = [[None for v in valves] for w in valves]
  

  for valve in valves:
    distances = valves_distances[indexes[valve]]
    for valve_near in valves[valve][1]:
      distances[indexes[valve_near]] = 1
      distances[indexes[valve]] = 0
  for iter in range(len(valves)):
    for i in range(len(valves)):
      for j in range(len(valves)):
        for k in range(len(valves)):
          d_i_k = valves_distances[i][k]
          d_k_j = valves_distances[k][j]
          d_i_j = valves_distances[i][j]
          if d_i_k and d_k_j:
            valves_distances[i][j] = min(d_i_j,d_i_k + d_k_j) if not d_i_j is None else d_i_k + d_k_j
  return valves_distances

valve_distances = calculate_distances()


def part1(current='AA',current_time=1,free_p_f_minute=0,free_p=0,opened=None,solutions=None):
  if not opened:
    opened = set()
  if not solutions:
    solutions = list()
  current_index = indexes[current]
  max_time = 30
  next_moves = []
  if len(opened) == len(valves):
    free_p += free_p_f_minute * (max_time - current_time)
    return free_p
  for valve in valves:
    if valve in opened or valve==current:
      pass
    else:
      valve_object = valves[valve]
      valve_index = indexes[valve]
      d = valve_distances[current_index][valve_index]
      if valve_object[0]*(max_time-current_time-d)>0:
        next_moves.append((valve,d,valve_object[0]))
  max_result = free_p
  if not next_moves:
    free_p += free_p_f_minute * (max_time+1 - current_time)
    return free_p
  for next_valve,d,p,*stuff in next_moves:
    free_p_b = free_p + free_p_f_minute * (d + 1)
    free_p_f_minute_b = free_p_f_minute + p
    current_index = indexes[next_valve]
    current_b = next_valve
    current_time_b = current_time + d + 1
    opened_b = deepcopy(opened)
    opened_b.add(current)
    solutions_b = deepcopy(solutions)
    solutions_b.append((current_b,current_time_b))
    max_result = max(max_result,part1(current_b,current_time_b,free_p_f_minute_b,free_p_b,opened_b,solutions_b))
  free_p = max_result
  return free_p

print(part1())
