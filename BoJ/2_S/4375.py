def fun(integer):
	for i in range(10000):
		str = int('1' * (i + 1))
		if str % int(integer) == 0:
			print(i + 1)
			break


while 1:
	try:
		ins = input()
		if ins == '0':
			print('0')
			break
		ans = fun(ins)
		if ans == -1:
			break
	except EOFError:
		break