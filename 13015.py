# 높이는 입력 * 2 -1
# 중간은 높이 // 2
# 가로는 입력 * 2 + 중간 * 2 -1
# 맨위, 맨끝이 아니라면 양 끝 공백은 '높이중간값' - 절대값('높이중간값' - '현재 높이')
# 맨위와 맨끝은 '높이 인덱스, 높이 인덱스 + 사이값 인덱스 + 1, 뒤에서 - 1 -공백값, 뒤에서 -공백값 -2 - 사이값 인덱스' 의 범위 내에 있으면 *
# 맨위와 맨밑이 아니면, '높이 인덱스, 높이 인덱스 + 사이값 인덱스 + 1, 뒤에서 - 1 -공백값, 뒤에서 -공백값 -2 - 사이값 인덱스' 에 해당하면 *
# 단, 뒤에 공백이 없어야 하므로, 마지막 * 인덱스보다 크면 answer 에 추가하지않고, 넘어간다

import sys

a = int(sys.stdin.readline())
n = a*2 - 1
b = a * 2 + (n // 2) * 2 -1
blank = a - 2
for i in range(n):
    answer = ''
    for j in range(b):
        if i == 0 or i == (n - 1):
            if (j >= 0 and j <= a-1) or (j >= (b-2-blank) and j <= (b - 1 )):
                answer += '*'
            else:
                answer += ' '
        else:
            locate = n // 2 - abs(n // 2 - i)
            if j in [locate, locate + blank + 1,b - locate - 1 , b - locate - blank - 2]:
                answer += '*'
            elif j > ( b - locate - 1):
                continue
            else:
                answer += ' '
    print(answer)
