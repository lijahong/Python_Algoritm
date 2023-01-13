# 크로아티아 알파벳 문제
# replace 를 통해 변환된 문자를 구분하고, 문자열 길이 반환
import sys
input = sys.stdin.readline

a = input().strip('\n')
a = a.replace('c=','A')
a = a.replace('c-','B')
a = a.replace('dz=','C')
a = a.replace('d-','D')
a = a.replace('lj','E')
a = a.replace('nj','F')
a = a.replace('s=','G')
a = a.replace('z=','Z')
print(len(a))
