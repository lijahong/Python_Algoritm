import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
orderlist = list()
for _ in range(n):
    orderlist.append(input().strip())


#orderlist = ["ORDER_2_C","ORDER_15_C","DONE_B","ORDER_7_C","ORDER_4_C","DONE_A","ORDER_8_B","DONE_B"]
#n = 8
a = deque()
b = deque()

for i in orderlist:
    arr = i.split('_')
    if arr[0] == "DONE":
        if arr[1] == "B":
            b.popleft()
        else:
            a.popleft()
    else:
        if arr[2] == "A":
            a.append(int(arr[1]))
        elif arr[2] == "B":
            b.append(int(arr[1]))
        else:
            if sum(a) > sum(b):
                b.append(int(arr[1]))
            else:
                a.append(int(arr[1]))

print("{}_{}".format(sum(a),sum(b)))
