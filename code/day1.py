#part 1
increases = 0
prev = 0
with open('../inputs/day1.txt', 'r') as f:
    for i in f.readlines()[1:]:
    	if int(i) > prev:
    		increases += 1
    	prev = int(i)
print(increases)

#part 2
increases = 0
prev = 0
with open('../inputs/day1.txt', 'r') as f:
    lines = list(map(int,f.readlines()))
    a = zip(lines, lines[1:], lines[2:])
    for i in a:
        if prev:
            increases += sum(i) > prev
        prev = sum(i)
        
    	
print(increases)