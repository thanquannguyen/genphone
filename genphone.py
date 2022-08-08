bin = '012'
def range9():
	rt = 10 - len(bin)
	rt = '9' * rt
	return int(rt)

# print(range9())
def add0(num):
	n = ''
	for x in range(num):
		n = n + '0'
	return (n)
def genPhone(bin):
	arr = []
	for i in range(range9()):
		rs = bin + str(i)
		if (len(rs) == 10):
			arr.append(rs + ":123456\n")
		else:
			arr.append(bin + add0(10 - len(rs)) + str(i) + ":123456\n")
	return arr		
phone = genPhone(bin)	
for i in phone:
	f = open("sdt.txt", "a")
	f.write(i)
	f.close()	
	f = open("sdt.txt", "r")
	print(f.read())

