#part 1
with open('../inputs/test.txt', 'r') as f:
	lines = f.readlines()
	total = len(lines)
	#will only count the 1s in each 'column'
	a = [0] * len(lines[0].strip())
	for line in lines:
		for i in range(0,len(line)-1):
			if int(line[i]):
				a[i] = a[i]+1
	gamma = ''.join(['1' if num > total/2 else '0' for num in a])
	epsilon = ''.join(['1' if num < total/2 else '0' for num in a])
	#epsilon = [1 if num == 0 else 0 for num in gamma]
	i_gamma = int(gamma, 2)
	i_epsilon = int(epsilon,2)
	print(i_epsilon * i_gamma)




#part 2    
#with open('../inputs/test.txt', 'r') as f:
