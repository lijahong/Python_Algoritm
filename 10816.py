import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
numlist = list(map(int,input().split()))

m = int(input())
findlist = list(map(int,input().split()))

numlist.sort()

for i in findlist:
    a = bisect_left(numlist,i)
    b = bisect_right(numlist,i)
    print( b - a, end = ' ')
