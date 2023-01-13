# n 진법에서 10 진법으로 -> n의 (전체길이 -1 - 현재 자리수 위치 )제곱 * 현재 자리수
# 10 진법에서 n진법으로 -> 해당 수가 0 보다 작을때까지 나머지를 문자열에 넣고, tmp 는 몫으로 덮어씌운다. 반복 종료 후, 뒤집으면 된다

def solution(s1, s2, p, q):
	answer = ''
	s1for10 = 0
	for i in range(len(s1)):
		s1for10 += (p ** (len(s1)-1-i)) * int(s1[i])
	s2for10 = 0
	for i in range(len(s2)):
		s2for10 += (p ** (len(s2)-1-i)) * int(s2[i])
	tmp = s1for10 + s2for10
	while tmp > 0:
		answer += str(tmp % q)
		tmp //= q
	answer = answer[::-1]

	return answer
