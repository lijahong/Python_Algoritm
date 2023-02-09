# https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
# 레벨3_bfs 문제
# 변환 불가 경우 -> words에 있는 단어로만 바꾸며 갈 수 있으므로, words에 target이 없으면 변환 불가

from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    answer = bfs(begin,target,words)
    return answer

def bfs( begin, target ,words):
    # begin을 넣는 이유는 방문 값을 증가시키기 위해서이다. 다른 count와 같은 변수를 통해 값을 설정하면, 값을 pop할 때마다 증가하기에, 
    # 정답을 향한 경우가 아닌 경우에 증가한 방문 값이 정답을 향한 경우의 방문 값에 영향을 줄 수 있다.
    # 따라서 이전 방문 값 + 1 하기 위해, begin을 words에 넣고, 방문 값을 1로 설정한다. 1로 설정하는 이유는 또 방문하지 않기 위해서 이다.
    words.append(begin)
    visit = [0 for _ in range(len(words))]
    visit[words.index(begin)] = 1
    queue = deque([begin])
    
    while queue:
        text = queue.popleft()
        # words에 있는 단어를 모두 비교한다.
        for comt in words:
            tcount = 0
            # 한자리만 바꿀 수 있으므로, 한자리만 다른지 확인한다.
            for i in range(len(text)):
                if text[i] != comt[i]:
                    tcount += 1
            # 한자리만 다르고, 방문하지 않았다면, 방문해야할 큐에 추가하고, 해당 노드의 방문값을 현재 노드의 방문값 + 1 로 설정한다.
            if tcount == 1 and visit[words.index(comt)] == 0:
                queue.append(comt)
                visit[words.index(comt)] = visit[words.index(text)] + 1
    # 처음 시작이 1이었으므로 1 빼야한다.
    return visit[words.index(target)] - 1
