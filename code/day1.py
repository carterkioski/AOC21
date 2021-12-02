increases = 0
prev = 0
with open('../inputs/day1.txt', 'r') as f:
    for i in f.readlines():
    	if not prev:
    		prev = int(i)
    		continue
    	if int(i) > prev:
    		increases += 1
    	prev = int(i)
print(increases)