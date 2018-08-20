from functools import reduce
def str2int(s):
	# def fn(x, y):
	# 	return x * 10 + y
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	# return reduce(fn, map(char2num, s))
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('123'))

def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def char2decimal(s):
		return {'0':0.0, '1':0.1, '2':0.2,'3':0.3, '4':0.4, '5':0.5,'6':0.6,'7':0.7,'8':0.8,'9':0.9}[s]
	n1 = reduce(lambda x,y:x*10+y,map(char2num,s.split('.')[0]))
	n2 = reduce(lambda x,y:x/10+y,map(char2decimal,s.split('.')[0]))
	return n1+n2
print(str2float('12.34'))
print(str2float('12.00'))