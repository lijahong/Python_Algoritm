step = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]

a = input()
x = int(ord(a[0])) - int(ord('a')) + 1
y = int(a[1])
count = 0
for i in step:
    mx = x + i[0]
    my = y + i[1]
    if mx < 1 or mx > 8 or my < 1 or my > 8:
        continue
    count += 1

print(count)
