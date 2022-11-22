import time
start = time.time()

n,m,k = map(int, input().split())
data = list(map(int,input().split()))
result = 0
data.sort(reverse=True)
while True:
    for i in range(k):
        if m == 0:
            break
        result += data[0]
        m -=1
    if m ==0 :
        break
    result += data[1]
    m -=1
print(result)

ed = time.time()
print(ed - start)
