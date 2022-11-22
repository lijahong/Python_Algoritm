n = int(input())
d = input().split()

a, b = 1, 1

mx = [0,0,-1,1]
my = [-1,1,0,0]
plan = ['L','R','U','D']

for i in d:
    for j in range(len(plan)):
        if i == plan[j]:
            x1 = a + mx[j]
            y1 = b + my[j]
    if x1 < 1 or x1 > n or y1 < 1 or y1 > n:
        continue
    a = x1
    b = y1

print(a, b)
