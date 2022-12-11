import sys

user_input = sys.stdin.readlines()
his_move = {
	'A': 1,
	'B': 2,
	'C': 3
}

my_move = {
	'X': 1,
	'Y': 2,
	'Z': 3
}

total_my_point = 0
for line in user_input:
	his, my = line.strip().split(' ')
	his_point = his_move[his]
	my_point = my_move[my]
	tot_turn_my = my_point
	if my_point == his_point + 1 or my_point + 3 == his_point + 1:
		tot_turn_my += 6
	elif my_point == his_point:
		tot_turn_my += 3
	else:
		pass
	
	total_my_point += tot_turn_my

print(f'first part {total_my_point}')

total_my_point = 0
for line in user_input:
	his, my = line.strip().split(' ')
	his_point = his_move[his]
	my_point = my_move[my]
	if my_point == 1:
		my_point = (his_point - 1 - 1 + 3) % 3 + 1
	elif my_point == 2: 
		my_point = his_point
	else:
		my_point = (his_point - 1 + 1) % 3 + 1
	tot_turn_my = my_point
	if my_point == his_point + 1 or my_point + 3 == his_point + 1:
		tot_turn_my += 6
	elif my_point == his_point:
		tot_turn_my += 3
	else:
		pass
	total_my_point += tot_turn_my

print(f'second part {total_my_point}')