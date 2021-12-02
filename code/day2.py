#part 1
x = 0
y = 0
with open('../inputs/day2.txt', 'r') as f:
	directions = [t.split() for t in f.readlines()]
	for direction in directions:
		if direction[0] == 'forward':
			x += int(direction[1])
		elif direction[0] == 'up':
			y += int(direction[1])
		elif direction[0] == 'down':
			y -= int(direction[1]) 

print(abs(x * y))



#part 2    
x = 0
y = 0
aim = 0
with open('../inputs/day2.txt', 'r') as f:
	directions = [t.split() for t in f.readlines()]
	for direction in directions:
		if direction[0] == 'forward':
			x += int(direction[1])
			y += int(direction[1]) * aim
		elif direction[0] == 'up':
			aim -= int(direction[1])
		elif direction[0] == 'down':
			aim += int(direction[1]) 
print(abs(x * y))