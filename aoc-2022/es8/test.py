import sys



user_input = map(lambda line: line.strip(),sys.stdin.readlines())

tree_grid = list(map(lambda line: list(map(lambda tree: int(tree),line)),user_input))

h = len(tree_grid)
w = len(tree_grid[0])

visible = set()

tree_grid_traspost = list(map(lambda j: [tree_grid[i][j] for i in range(h)],range(w)))

for i in range(h):
	for j in range(w):
		tree_index = f'{i}_{j}'
		if i == 0 or j == 0 or i == h - 1 or j == w - 1:
			visible.add(tree_index)
		else:
			tree_h = tree_grid[i][j]
			if max(tree_grid[i][j+1:]) < tree_h or max(tree_grid[i][:j]) < tree_h:
				visible.add(tree_index)
			else:
				if max(tree_grid_traspost[j][i+1:]) < tree_h or max(tree_grid_traspost[j][:i]) < tree_h:
					visible.add(tree_index)


max_spot = 0

def sum_spot(tree_h,otherTrees):
	current_spot = 0
	for an_h in otherTrees:
		current_spot += 1
		if an_h >= tree_h:
			break
	return current_spot


for i in range(h):
	for j in range(w):
		current_spot = 0
		tree_h = tree_grid[i][j]
		current_spot = sum_spot(tree_h, tree_grid[i][j+1:]) * sum_spot(tree_h,tree_grid[i][:j][::-1])
		current_spot *= sum_spot(tree_h, tree_grid_traspost[j][i+1:]) * sum_spot(tree_h, tree_grid_traspost[j][:i][::-1])
		if current_spot > max_spot:
			max_spot = current_spot

print(len(visible))
print(max_spot)
