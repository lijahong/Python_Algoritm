# 문자열 순서에 따라 반복문을 두 번 진행한다. 앞 뒤 슬라이싱 범위를 통해 비교하는데, 비교의 시작 부분은 정해져 있다.
# 동일하지 않으면 값을 저장하지 않으므로, 최대 동일 범위 값만 저장된다.
# 두번째에서는 첫번째의 결과보다 클때만 값을 저장하게 한다.

def solution(s1, s2):
	answer = 0
	for i in range(len(s1)):
		if s1[0:i] == s2[-i:]:
			answer = i
			
	for i in range(len(s2)):
		if s2[0:i] == s1[-i:]:
			answer = max(answer,i)
	
	answer = len(s1) + len(s2) - answer	
	return answer
