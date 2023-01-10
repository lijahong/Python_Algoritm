# 한줄에 입력가능한 문자수를 정하고, 배열에 담긴 문자들을 모두 적을 때, 총 몇줄이 필요한지 출력

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(K, words):
    # 여기에 코드를 작성해주세요.
    answer = 1
    currentnum = K
    for i in words:
        if currentnum >= len(i):
            currentnum -= len(i) + 1
        else:
            answer += 1
            currentnum = K
            currentnum -= len(i) + 1
        
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
