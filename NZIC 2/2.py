drop_offs = int(input())

current = drop_offs
for i in range(drop_offs):
	n = int(input())

	current += n

if current == drop_offs:
	print("She's got them all")
else:
	print(drop_offs - current)