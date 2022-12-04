import sys
import string



user_input = sys.stdin.readlines()

count_fully_contains = 0
count_overlaps = 0
for line in user_input:
	first, second = map(lambda assign: list(map(int,assign.split('-'))),line.strip().split(','))
	first_set = set(list(map(str,range(first[0],first[1] + 1))))
	second_set = set(list(map(str,range(second[0],second[1] + 1))))
	
	if first_set.issubset(second_set) or first_set.issuperset(second_set):
		count_fully_contains += 1
	symmetric_difference = set.symmetric_difference(first_set,second_set)
	count_overlaps += (len(symmetric_difference) != len(first_set) + len(second_set))

print(count_fully_contains)
print(count_overlaps)