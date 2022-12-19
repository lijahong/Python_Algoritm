#2022 카카오 테크 인턴쉽 성격 유형 검사하기
def solution(survey, choices): 
    answer = ''
    dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):  
        if choices[i] - 4 > 0:
            dic[survey[i][1]] += abs(choices[i] - 4)
        elif choices[i] - 4 < 0:
            dic[survey[i][0]] += abs(choices[i] - 4)
    keyarray = list(dic.keys())
    for i in range(0,8,2):
        if dic.get(keyarray[i]) > dic.get(keyarray[i+1]):
            answer += keyarray[i]
        elif dic.get(keyarray[i]) == dic.get(keyarray[i+1]):
            answer += keyarray[i]
        else:
            answer += keyarray[i+1]
    return answer
