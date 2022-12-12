import sys


user_input = map(lambda line: line.strip(),sys.stdin.readlines())

user_input_matrix = list(map(lambda line: list(line),user_input))

h = len(user_input_matrix)
w = len(user_input_matrix[0])

start = None
end = None
for i in range(h):
	for j in range(w):
		if user_input_matrix[i][j] == 'S':
			start = (i,j)
			user_input_matrix[i][j] = 'a'
		elif user_input_matrix[i][j] == 'E':
			end = (i,j)
			user_input_matrix[i][j] = 'z'
		user_input_matrix[i][j] = int(user_input_matrix[i][j],36)


def get_distances(start):
	distances = [[None for j in range(w)] for i in range(h)]
	to_visit = [start]
	x, y = start
	distances[x][y] = 0

	while True:
		if len(to_visit) == 0:
			break
		x, y = to_visit.pop(0)
		future_d = distances[x][y] + 1
		possible_h = user_input_matrix[x][y] + 1
		if x + 1 < h and possible_h >= user_input_matrix[x+1][y]:
			if distances[x+1][y] is None:
				to_visit.append((x+1,y))
				distances[x+1][y] =  future_d
			elif distances[x+1][y] > future_d:
				distances[x+1][y] = future_d
		if x - 1 > -1 and possible_h >= user_input_matrix[x-1][y]:
			if distances[x-1][y] is None:
				to_visit.append((x-1,y))
				distances[x-1][y] = future_d
			elif distances[x-1][y] > future_d:
				distances[x-1][y] = future_d
		if y + 1 < w and possible_h >= user_input_matrix[x][y+1]:
			if distances[x][y+1] is None:
				to_visit.append((x,y+1))
				distances[x][y+1] =  future_d
			elif distances[x][y+1] > future_d:
				distances[x][y+1] = future_d
		if y - 1 > -1 and possible_h >= user_input_matrix[x][y-1]:
			if distances[x][y-1] is None:
				to_visit.append((x,y-1))
				distances[x][y-1] = future_d
			elif distances[x][y-1] > future_d:
				distances[x][y-1] = future_d
	return distances

distances = get_distances(start)

x,y = end
print(distances[x][y])




for i in range(h):
	for j in range(w):
		user_input_matrix[i][j] = int('z',36) + int('a',36) - user_input_matrix[i][j]


distances = get_distances(end)
a_h_distances = []

for i in range(h):
	for j in range(w):
		if user_input_matrix[i][j] == int('z',36) and distances[i][j]:
			a_h_distances.append(distances[i][j])


print(min(a_h_distances))