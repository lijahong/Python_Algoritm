def solution(genres, plays):
    answer = []
    # 음악 종합 리스트 만들기
    music_list = []
    for i,j in enumerate(genres):
        music_list.append([i,j,plays[i]])
    # 장르별 누적합 구하기
    set_music = list(set(genres))
    dict_music = {}
    for i in set_music:
        dict_music[i] = 0
    for j_index,j in enumerate(genres):
        dict_music[j] += plays[j_index]
    genres_rank = sorted(list(dict_music.items()), reverse = True, key=lambda x:x[1])
    for i,j in enumerate(genres_rank):
        for x,y in enumerate(music_list):
            if y[1] == j[0]:
                music_list[x][1] = i
    music_list.sort(key = lambda x:(x[1],-x[2]))
    countlist = [0] * len(genres_rank)
    for i in music_list:
        if countlist[i[1]] == 2:
            continue
        else:
            answer.append(i[0])
            countlist[i[1]] += 1
    
    return answer
