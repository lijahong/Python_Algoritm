# 순열 : 중복없이 뽑되, 순서에 상관 있이 / 조합 : 중복없이 뽑되, 순서에 상관 없이
# 순열 라이브러리를 쓰면, 튜플로 반환하기에, 이를 문자열로 만들고, int 로 반환하여 리스트에 넣는다
# 정렬 후, 순서 출력

from itertools import permutations
def solution(card, n):
	answer = 0
	arr = list(permutations(card,4))
	arr2 = list()
	for i in range(len(arr)):
		lin = ''
		for j in range(4):
			lin += str(arr[i][j])
		if int(lin) not in arr2:
			arr2.append(int(lin))
	arr2.sort()
	for i in range(len(arr2)):
		if arr2[i] == n:
			answer = i + 1
	if answer == 0:
		answer = -1
	return answer
