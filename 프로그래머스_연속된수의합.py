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
