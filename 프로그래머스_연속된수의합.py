# https://school.programmers.co.kr/learn/courses/30/lessons/120923?language=python3
# 수학 문제 인거 같다. 다른 사람 풀이 보면 시작 수를 공식으로 구해서, num 만큼 반복문으로 더해서 배열에 집어넣는다.
def solution(num, total):
    answer = []
    mid = total // num
    answer.append(mid)
    for i in range(1,num // 2 + 1):
            if i == num // 2:
                if num % 2 == 0:
                    if (sum(answer) + mid + i) == total:
                        answer.append(mid + i)
                    if (sum(answer) + mid - i) == total:
                        answer.append(mid - i)
                else:
                    answer.extend( [ mid + i, mid - i ])
            else:
                answer.extend( [ mid + i, mid - i ])
    answer.sort()  
    return answer

### 다른 풀이
# 시작 수를 구하는 법 : 평균을 구해서 시작 수를 균등하게 맞추는 방법도 있다.
# 홀수인 경우, 34567일때, 5가 나오고, 3456일때, 4.5가 나온다. 시작 수를 3으로 맞추려면, ( num - 1 ) / 2 를 통해 각각 2와 1.5 를 빼줘서 3으로 맞출 수 있다.
# 이후 num 만큼 반복하며 수를 키워서 정답 배열에 넣으면 된다.
