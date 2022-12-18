import sys
from copy import deepcopy

user_input = map(lambda line: line.strip(), sys.stdin.readlines())

lava_cubes = set()

for line in user_input:
    lava_cubes.add(tuple(map(int,line.split(','))))

def get_cube_faces_set(cube):
    result = set()
    for i in range(len(cube)):
        result.add(cube[:i] + ((cube[i],cube[i] + 1),)+ cube[i+1:])
        result.add(cube[:i] + ((cube[i] - 1,cube[i]),)+ cube[i+1:])
    return result
cube_faces_set_list = list(map(get_cube_faces_set,lava_cubes))



faces_union = set.union(*cube_faces_set_list)
result = deepcopy(faces_union)

for i in range(len(lava_cubes)):
    for j in range(len(lava_cubes)):
        if i != j:
            result.difference_update(cube_faces_set_list[i].intersection(cube_faces_set_list[j]))

print(len(result))


def check_max_min(index_1,index_2,index_to_max):
    result_min = {}
    result_max = {}
    for cube in lava_cubes:
        i, j, current = cube[index_1], cube[index_2], cube[index_to_max]
        if (i,j) in result_min:
            result_min[(i,j)] = min(result_min[(i,j)],current)
            result_max[(i,j)] = max(result_max[(i,j)],current)
        else:
            result_min[(i,j)] = current
            result_max[(i,j)] = current
    return result_min, result_max

min_z, max_z = check_max_min(0,1,2)
min_x, max_x = check_max_min(1,2,0)
min_y, max_y = check_max_min(0,2,1)



abs_max_z = max(max_z.values())
abs_max_y = max(max_y.values())
abs_max_x = max(max_x.values())
abs_min_z = min(min_z.values())
abs_min_y = min(min_y.values())
abs_min_x = min(min_x.values())

air_cubes = set()

for face in faces_union:
    tuple_index = None
    for i in range(len(face)):
        if type(face[i]) == tuple:
            tuple_index = i
    possible_cubes = [face[:tuple_index] + (face[tuple_index][0],) + face[tuple_index + 1:],face[:tuple_index] + (face[tuple_index][1],) + face[tuple_index + 1:]]
    for pos_cube in possible_cubes:
        if not pos_cube in lava_cubes:
            x, y , z = pos_cube
            if abs_min_x < x < abs_max_x and abs_min_y < y < abs_max_y and abs_min_z < z < abs_max_z:
                if (x,y) in min_z and min_z[(x,y)] < z < max_z[(x,y)]:
                    if (x,z) in min_y and min_y[(x,z)] < y < max_y[(x,z)]:
                        if (y,z) in min_x and min_x[(y,z)] < x < max_x[(y,z)]:
                            air_cubes.add(pos_cube)


to_remove_faces = set.union(*list(map(get_cube_faces_set,air_cubes)))

print(len(result.difference(to_remove_faces)))
