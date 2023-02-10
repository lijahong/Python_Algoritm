''' count를 통해 값을 지정한 방식
def solution(dartResult):
    answer = 0
    score = [0 for _ in range(3)]
    dartResult = dartResult.replace('10','A') # 10을 구분하기 위해서
    mult = ['S','D','T']
    checkten = '0'
    count = -1
    
    for i in dartResult:
        if i.isnumeric(): #만약 해당 문자가 수라면 count를 증가시키고, 값을 지정한다
            count += 1
            score[count] = int(i)
        elif i == 'A':
            count += 1
            score[count] = 10
            
        elif i in mult:
            score[count] = score[count] ** (mult.index(i) + 1)
        
        elif i == '*':
            if count >= 1:
                score[count] *= 2
                score[count-1] *= 2
            else:
                score[count] *= 2
        elif i == '#':
            score[count] *= -1
            
    answer = sum(score)
    return answer
 '''
# 더 나은 코드 -> 문자가 숫자라면 n에 추가하여 제곱 연산 후 배열에 추가한다. 이러면 10도 1과 0이 연속으로 오기에 10으로 연산이 가능하다
def solution(dartResult):
    answer = 0
    score = list()
    mult = ['S','D','T']
    n=''
    
    for i in dartResult:
        if i.isnumeric():
            n += i
            
        elif i in mult:
            n = int(n) ** (mult.index(i) + 1)
            score.append(n)
            n =''
        
        elif i == '*':
            if len(score) > 1:
                score[-1] *= 2
                score[-2] *= 2
            else:
                score[-1] *= 2
        elif i == '#':
            score[-1] *= -1
            
    answer = sum(score)
    return answer
