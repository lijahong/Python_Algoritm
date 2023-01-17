def solution(n):
	answer = 0
	
	arr = [[0 for _ in range(n)]for _ in range(n)]
	anwarr = list()
	row = 0 
	cul = -1
	cnt = 1
	trans = 1
	maxn = n ** 2
	tmp = n
	
	while cnt <= maxn:
		for i in range(n):
			cul += trans
			arr[row][cul] = cnt
			cnt += 1
		n -= 1
		for i in range(n):
			row += trans
			arr[row][cul] = cnt
			cnt += 1
		trans *= -1
	
	x,y = 0,0
	for i in range(tmp):
		anwarr.append(arr[x][y])
		x += 1
		y += 1
	answer = sum(anwarr)
	
	return answer
