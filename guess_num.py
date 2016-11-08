from random import *
import itertools

cla = set()
maps = {}
def force():
	lis = itertools.permutations([str(i) for i in range(10)],4)
	for i in lis:
		num = ''.join(list(i))
		yield num

def check(c):
	num = []
	while len(num) < 4:
		n = str(randint(0,9))
		if n not in num:
			num.append(n)
	num = ''.join(num)
	count = times = 0
	A = B = 0
	while True:
		guess = c.next()
		print('%d guess:%s'%(times+1,guess))
		A = B = 0
		for i in guess:
			if i in num:
				B += 1
				if i == num[guess.index(i)]:
					A += 1
		if A == 4 and B==4:
			print('correct! %s'%num)
			break
		print('A%dB%d'%(A,(B-A)))
		print('-'*20)
		times += 1
	print(num)

c = force()
check(c)