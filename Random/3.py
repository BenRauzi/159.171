bc = int(input())

t = 0

for i in range(bc):
	t += int(input())

if t < 60:
	print(f"It took {t} {'minutes' if t % 60 != 1 else 'minute'}")
else:
	print(f"It took {t//60} {'hours' if t // 60 > 1 else 'hour'} {(f'and {t % 60} ' + ('minutes' if t % 60 != 1 else 'minute')) if t % 60 > 0 else ''}")