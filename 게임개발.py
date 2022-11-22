n,m = map(int,input().split())

d = [[0] * m for _ in range (n)]
x,y,direction = map(int,input().split())

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1, 0 ,1, 0]
dy = [0,1,0,-1]
d[x][y] = 1
def turnleft():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

count = 1
turntime = 0

while True:
    turnleft()
    x1 = x + dx[direction]
    y1 = y + dy[direction]

    if d[x1][y1] == 0 and array[x1][y1] == 0:
        d[x1][y1] == 1
        x = x1
        y = y1
        d[x1][y1] = 1
        count += 1
        turntime = 0
    else:
        turntime += 1
    if turntime > 3:
        x1 = x - dx[direction]
        y1 = y - dy[direction]
        if array[x1][y1] == 1:
            break
        x,y = x1,y1
        turntime = 0
print(count)
