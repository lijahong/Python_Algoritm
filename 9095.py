import sys
input = sys.stdin.readline

n = int(input())
num = list()
for i in range(n):
    num.append(int(input()))

answer = [[] for _ in range(n)]
numlist = [1,2,3]

def search(j,num2):
    for i in numlist:
        if (j - i) == 0:
            answer[num2].append(1)
        elif (j -i) > 0:
            search(j-i,num2)

for i in range(n):
    search(num[i],i)
    print(sum(answer[i]))
