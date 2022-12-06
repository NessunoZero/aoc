import sys
import string



user_input = sys.stdin.readlines()

def after_n_different(n):
	message = user_input[0]
	for i in range(0,len(message)):
		four_different = ''
		for j in range(i,len(message)):
			c = message[j]
			if not c in four_different:
				four_different += c
			else:
				break
			if len(four_different) == n:
				break
		if len(four_different) == n:
			break
	print(j + 1)	

after_n_different(4)
after_n_different(14)