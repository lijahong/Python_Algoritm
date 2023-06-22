# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# 2진수 변환 라이브러리 bin을 사용하면, 쉽게 2진수 변환을 할 수 있다. bin을 사용하면, 각 진수 형태의 문자열을 반환해준다. 따라서 bin 라이브러리의 결과를 이용해 계산을 하려면, 숫자로 변환해야 한다
# 파이썬에서 수가 2진수인지 나타내려면, 앞에 0b 를 붙여야 한다. 1101은 10진수 지만, 0b1101은 2진수이다
# 비트연산자 & , | 은 10진수 사이에서도 연산 가능하다. 자동으로 해당 10진수를 2진수로 변환하여 비트연산해준다

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer_row = ''
        answer_row_num_10 = (arr1[i] | arr2[i])
        answer_row_binary = bin(answer_row_num_10)[2:]
        if len(answer_row_binary) < n :
            answer_row_binary = '0' * (n - len(answer_row_binary)) + answer_row_binary
        for j in range(n):
            if answer_row_binary[j] == '1':
                answer_row += '#'
            else:
                answer_row += ' '
        answer.append(answer_row)
    return answer     
