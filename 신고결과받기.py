#2022 카카오 블라인드 채용 - 신고 결과 받기 문제
def solution(id_list, report, k):
    answer = []
    dic1 = {}
    dic2 = {}
    
    for i in id_list:
        dic1[i] = {'count':0}
        dic2[i] = {'count':0}
        for j in id_list:
            dic1[i][j] = 0
     
    for i in report:
        calllist = i.split(' ')
        send = calllist[0]
        ben = calllist[1]
       
        if dic1[send][ben] == 0:
            dic1[ben]['count'] += 1
            dic1[send][ben] = 1
            
    for bname in id_list:
        if dic1[bname]['count'] >= k :
                for name in id_list:
                    if dic1[name][bname] == 1:
                        dic2[name]['count'] += 1
    for name in id_list:
        answer.append(dic2[name]['count'])
        
    return answer
