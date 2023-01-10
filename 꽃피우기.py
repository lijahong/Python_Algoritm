#2차원 배열을 전체 1로 바꾸는데 걸리는 시간 측정 문제, 1인 곳 주변을 1로 바꾼다

# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    x = [-1,0,1,0]
    y = [0,-1,0,1]
    lg = len(garden)
    next = []
    while len(next) < len(garden)**2 : #1의 개수가 정원의 크기와 같으면 스탑
        seed = 0
        next.clear()
        for i in range(lg):
            for j in range(lg):
                if garden[i][j] == 1:
                    next.append([i,j])
                    
        for nexta in next:
            for z in range(4):
                if( nexta[0] + x[z] ) < 0 or (nexta[1] + y[z]) >= lg or ( nexta[0] + x[z]) >= lg or (nexta[1] + y[z]) < 0:
                    continue
                if garden[nexta[0]+x[z]][nexta[1]+y[z]] == 0:
                    garden[nexta[0]+x[z]][nexta[1]+y[z]] = 1
                    seed = 1
        if seed == 1:
            answer += 1
            seed = 0            
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
