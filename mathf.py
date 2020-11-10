def double(x, understand = True):
	if x == 0 and understand == True:
		print('Did you mean to double something that is 0?')
	elif x <= 0:
		print('Did you mean to double a negative?')
	return 2*x
