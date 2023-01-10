# 뽑은 4가지 수에서 가장 큰수와 가장 작은수의 차이가 가장 작은 값을 구하시오
# 순열 라이브러리 -> 시간 초과
# 배열 정렬 후, 가장 작은 수에서 뽑아야하는 수 - 1 을 더한 순서의 값과 빼기 연산을 하여 구하면 된다

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(arr, K):
    # 여기에 코드를 작성해주세요.
    answer = max(arr)
    arr.sort()
    for i in range(0,len(arr)-K+1,1):
        answer = min(answer,arr[i+K-1] - arr[i])
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")
