i = int(input())
i = 1000 - i
coin = [500,100,50,10,5,1]
count = 0
for n in coin:
    count += i // n
    i %= n

print(count)
