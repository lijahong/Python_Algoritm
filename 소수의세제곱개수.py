# 아리스토에서 채걸러낼때는 무조건, 해당 수의 배수!!!! 2배 부터 시작해서 스스로 더해가면서 없앤다!
def alisto(b):
	sosuright = [False,False] + [True] * (b - 1)
	sosulist = list()
	for i in range(2,b + 1):
		if sosuright[i] == True:
			sosulist.append(i)
			for j in range(2*i,b+1,i):
				sosuright[j] = False
	return sosulist

def solution(a, b):
	answer = 0
	arr = alisto(b)

	for i in arr:
		if a<= i ** 2 <= b :

			answer += 1
		if a <= i ** 3 <= b:

			answer += 1
		
	return answer
