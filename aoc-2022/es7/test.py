import sys
import string



user_input = map(lambda line: line.strip(),sys.stdin.readlines())
file_system = {'/': {}}
path = ''

def access_file_system(path,write=False,to_write={}):
	tmp = file_system
	if path.endswith('/'):
		*paths, last = ['/',*path.split('/')[1:-1]]
	else:
		*paths, last = ['/',*path.split('/')[1:]]
	
	for dir in paths:
		tmp = tmp[dir]
	if(write):
		tmp[last] = to_write
	else:
		return tmp[last]

def process(command,output):
	global path
	if not command:
		return	
	if command[0] == 'cd':
		if command[1] == '/':
			path = '/'
		elif command[1] == '..':
			last_back_index = path.rfind('/')
			if last_back_index != 0:
				path = path[:last_back_index]
			else:
				path = '/'
		elif path.endswith('/'):
			path += command[1]
		else:
			path += f'/{command[1]}'
	elif command[0] == 'ls':
		for out_line in output:
			path_to_write = f'{path}{out_line[1]}' if path.endswith('/') else f'{path}/{out_line[1]}'
			if out_line[0] == 'dir':
				access_file_system(path_to_write,True,{})
			else:
				access_file_system(path_to_write,True,int(out_line[0]))
	else:
		print('unmanaged command')

size_dirs = {}
def folders_size(path = '/'):
	global size_dirs	
	sum_size = 0
	tmp_file_system = access_file_system(path)
	for key, value in tmp_file_system.items():
		if type(value)==int:
			sum_size += value
		else:
			sub_path = path + (key if path.endswith('/') else f'/{key}')
			
			sum_size += folders_size(sub_path)
	size_dirs[path] = sum_size
	return sum_size


last_command = []
output = []
for line in user_input:
	if line.startswith('$ '):
		process(last_command,output)
		last_command = line.split(' ')[1:]
		output = []
	else:
		output.append(line.split(' '))
process(last_command,output)

def part1():
	sum = 0
	for dir_size in size_dirs.values():
		sum += dir_size if dir_size <= 100000 else 0
	return sum

def part2():
	used_space = size_dirs['/']
	to_free_space = 30000000 - (70000000 - used_space)
	min_dir_size = used_space
	for dir_size in size_dirs.values():
		if dir_size >= to_free_space:
			if min_dir_size > dir_size:
				min_dir_size = dir_size
	return min_dir_size

	
folders_size()
print(part1())
print(part2())