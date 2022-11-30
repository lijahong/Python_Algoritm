import sys
input = sys.stdin.readline

n = int(input())
numlist = list(map(int,input().split()))

m = int(input())
findlist = list(map(int,input().split()))

def binary_search(start,end,find):
    if start > end:
        print("0")
        return None
    middle = (start + end) // 2
    if numlist[middle] == find:
        print("1")
        return None
    elif numlist[middle] > find:
        binary_search(start,middle-1,find)
    else:
        binary_search(middle+1,end,find)

# 일단 정렬하기. 이진 탐색은 정렬 상태가 전제조건이다
numlist.sort()
for i in findlist:
    result = binary_search(0,n-1,i)
