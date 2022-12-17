import sys


user_input = map(lambda line: line.strip(), sys.stdin.readlines())

gas_jets = list(user_input).pop()
len_gas_jets = len(gas_jets)

stones = [
    tuple((i, 0) for i in range(4)),
    tuple(((1, i) for i in range(3))) + ((0, 1), (2, 1)),
    tuple((i, 0) for i in range(3)) + tuple((2, j) for j in range(1, 3)),
    tuple((0, j) for j in range(4)),
    tuple((0, j) for j in range(2)) + tuple((1, j) for j in range(2))
]

stones_max_r = list(map(lambda stone: max(
    stone, key=lambda x: x[0])[0], stones))
stones_max_h = list(map(lambda stone: max(
    stone, key=lambda x: x[1])[1], stones))


def print_stones(stones):
    matrix = [[None for i in range(4)] for j in range(4)]

    for i in range(len(stones)):
        stone = stones[i]
        print('r_max:', stones_max_r[i])
        print('h_max:', stones_max_h[i])
        for i in range(4):
            for j in range(4):
                matrix[i][j] = '#' if (j, 3-i) in stone else '.'
        for line in matrix:
            print(''.join(line))
        print()


print_stones(stones)


def simulate_n_stones(n):
    grid = set()
    grid = grid.union(set((i, -1) for i in range(7)))
    max_y = 0
    current_jet = 0
    falling_h = 3
    len_stones = len(stones)

    for i in range(n):
        stone_index = i % len_stones
        stone = stones[stone_index]
        stone_max_h = stones_max_h[stone_index]
        stone_max_r = stones_max_r[stone_index]
        x, y = 3 - 1, max_y + falling_h
        iter = 0
        while y > max_y + 2:
            iter += 1
            current_jet = current_jet % len_gas_jets
            wind = 1 if gas_jets[current_jet] == '>' else -1
            current_jet += 1
            if x + wind >= 0 and x + wind + stone_max_r < 7:
                x, y = x + wind, y
            x, y = x, y - 1
        continue_placement = True
        while continue_placement:
            continue_placement = True
            iter += 1
            current_jet = current_jet % len_gas_jets
            wind = 1 if gas_jets[current_jet] == '>' else -1
            current_jet += 1
            if x + wind >= 0 and x + wind + stone_max_r < 7:
                can_continue = True
                for s in stone:
                    if (s[0] + x + wind, y+s[1]) in grid:
                        can_continue = False
                        break
                if can_continue:
                    x, y = x + wind, y
            can_continue = True
            for s in stone:
                if (s[0] + x, y+s[1]-1) in grid:
                    continue_placement = False
                    can_continue = False
                    break
            if can_continue:
                x, y = x, y - 1
        max_y = max(max_y, y + stone_max_h + 1)
        for s in stone:
            grid.add((x+s[0], y+s[1]))

    print('max_h:', max_y)


simulate_n_stones(2022)
