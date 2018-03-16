n = int(input())

end = 100
cur = 2
prev = 1

while cur <= end:
	print(cur)
	cur, prev = cur + prev, cur
