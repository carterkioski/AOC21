import re
#part 1
'''with open('../inputs/test.txt', 'r') as f:
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
	i_gamma = int(gamma, 2)
	i_epsilon = int(epsilon,2)
	print(i_epsilon * i_gamma)
'''



#part 2    
with open('../inputs/day3.txt', 'r') as f:
	lines = [line.strip() for line in f.readlines()]
item_len = len(lines[0])
o_lines = list(lines)
c_lines = list(lines)
oxygen = list()
carbon = list()
#will only count the 1s in each 'column'
def find_count(binaries, pos, type):
	count = 0
	total = len(binaries)
	for line in binaries:
		if int(line[pos]):
			count += 1
	if type == 'o':
		return '1' if count >= total/2 else '0'
	else:
		return '1' if count < total/2 else '0'



for i in range(0,item_len):
	if len(o_lines) > 1:
		oxygen.append(find_count(o_lines,i,'o'))
		o_r = re.compile(f'{"".join(oxygen)}.*')
		o_lines = list(filter(o_r.match,o_lines))
	else:
		oxygen = o_lines[0]

	if len(c_lines) > 1:
		carbon.append(find_count(c_lines,i,'c'))
		c_r = re.compile(f'{"".join(carbon)}')
		c_lines = list(filter(c_r.match,c_lines))
	else:
		carbon = c_lines[0]

print(int(''.join(oxygen),2) * int(''.join(carbon),2))