import sys
input = sys.stdin.readline

n = int(input())
stack = list()
answer = list()
pos = 1 # 넣을 수

for _ in range(1,n+1):
    m = int(input())
    while pos <= m:
        stack.append(pos)
        answer.append("+")
        pos += 1
    if stack[-1] == m:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit(0)
for i in answer:
    print(i)
