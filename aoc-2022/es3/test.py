import sys
import string


alphabet = string.ascii_letters
values_dict = {alphabet[i]:i+1 for i in range(len(alphabet))}

user_input = sys.stdin.readlines()

common_sum = 0
for line in user_input:
	tmp_line = line.strip()
	two_part = tmp_line[:len(tmp_line)//2], tmp_line[len(tmp_line)//2:]
	first, second = map(set,two_part)
	middle_one = first.intersection(second).pop()
	common_sum += values_dict[middle_one]

badge_group_sum = 0
for index in range(0,len(user_input),3):
	lines = user_input[index:index+3]
	tmp_lines = map(lambda line: line.strip(),lines)
	three_lines = map(set,tmp_lines)
	middle_one = set.intersection(*three_lines).pop()
	badge_group_sum += values_dict[middle_one]

print(common_sum)
print(badge_group_sum)
