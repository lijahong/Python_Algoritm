import sys
input = sys.stdin.readline

a,b = map(int,input().split())
ans = []

def backtracking(): # 배열 길이로 비교
    if len(ans) == b: # 만약, ANS 길이가 모아야하는 수열의 크기와 같다면
        print(" ".join(map(str,ans))) # 수열 출력
        return
    for i in range(1,a+1): # 넣을 수 있는 모든 자식 노드의 가능성
        if i not in ans: # 현재 수열에 중복되는 원소가 아니라면
            ans.append(i) # 넣기
            backtracking() # 재귀
            ans.pop() # 넣은거 없애기

visited = [False] * (a+1)
def back(depth,n,m): # VISITED 와 DEPTH 사용
    if depth == m:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,n+1):
        if visited[i] == False: # 탐색이 아니라 걍 방문 여부 확인
            visited[i] = True
            ans.append(i)
            back(depth+1,n,m) # DEPTH 를 늘려서 수열의 길이가 늘어남을 알려준다. 이를 통해 재귀
            visited[i] = False
            ans.pop()
back(0,a,b)
