# 두줄만 쓰라고 해서 헷갈렸는데, 그냥 자리수 문제는 10으로 나머지 연산하면 오른쪽 끝자리가 나오고, 10 으로 몫 연산해서 덮어씌우면 오른쪽 끝자리가 사라진다.

def power(base, exponent):
	val = 1
	for i in range(exponent):
		val *= base
	return val

def solution(k):
	answer = []
	bound = power(10, k)
	for i in range(bound // 10, bound):
		current = i
		calculated = 0
		while current != 0:
			calculated += power(current % 10,3)
			current //= 10
		if calculated == i:
			answer.append(i)
	return answer
