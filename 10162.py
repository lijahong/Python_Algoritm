import sys

n = int(sys.stdin.readline())

t = [300,60,10]
c = [0,0,0]

if n % 10 != 0:
    print(-1)
    sys.exit()
else:
 for i in range(len(t)):
    if n//t[i] > 0:
        c[i] = n//t[i]
        n %= t[i]

print(*c)
sys.exit()
