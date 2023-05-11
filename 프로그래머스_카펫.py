# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 가운데 노란색에 대한 완전탐색을 하면 된다. 가운데 사각형의 가로 + 2 는 바깥 사각형의 가로이고, 가운데 사각형의 세로 + 2 는 바깥 사각형의 세로인 것을 기억하자
def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            x = yellow // i
            y = i
            if ( x + 2) * (y + 2) == (brown + yellow):
                    answer.append(x + 2)
                    answer.append(y + 2)
                    break
    return answer
