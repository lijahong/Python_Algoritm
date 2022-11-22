n, m = map(int, input().split())

count = 0

while True:
  if ( n%m == 0):
      if( n == 1):
          break
      n /= m
      print(n)
      count += 1
  else:
    if(n == 1):
        break
    n -= 1
    count +=1

print(count)
