# 실수형 반올림
a=123.456
print(round(a, 2))


# 1차원 리스트
array = [0]*3
# [0,0,0]


# 2차원 리스트 N*M
N, M = 3, 5
array1 = [[0]*M for _ in range(N)]
#[[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

# remove 함수는 특정 값 하나만 제거
a=[1,2,3,4,5,5,5]
remove_set={3, 5}
result = [i for i in a if i not in remove_set]
print(result)
# [1,2,4]


##### 자주 사용하는 리스트 관련 함수 #####
# append()  : 원소 하나 추가
# sort()    : 정렬(default=오름차순)(reverse=True 하면 내림차순)
# reverse() : 원소 순서 뒤집기
# insert()  : 특정 위치에 삽입(삽입할 위치 인덱스, 삽입할 값)
# count()   : 특정값 가지는 데이터 개수(특정값)
# remove()  : 특정 원소 제거(특정값)(특정값 가진 원소 여러개여도 하나만 제거)


##### 집합 자료형 연산
set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])
# 합집합 {1,2,3,4,5,6,7}
print(set1 | set2)
# 교집합 {3,4,5}
print(set1 & set2)
# 차집합 {1,2}
print(set1 - set2)


##### 집합 자료형 변수
data = set([1,2,3])
print(data)
# {1,2,3}

# 원소 추가
data.add(4)
print(data)
{1,2,3,4}

# 원소 여러 개 추가
data.update([5,6])
print(data)
{1,2,3,4,5,6}

# 특정 값 갖는 원소 삭제
data.remove(6)
print(data)
{1,2,3,4,5}

# 없는 값 remove 할 시 에러 발생
data.remove(7)


##### 입력 받기 #####
aa = input() # 문자열 형태로 입력 됨
bb = int(input()) # int 형태로 변환
cc = list(map(int, input().split())) # 공백을 기준으로
aaa, bbb, ccc = map(int, input().split()) # 입력이 3개로 주어진 경우

##### 빠른 입력 받기 #####
import sys
data = sys.stdin.readline().rstrip()
print(data)


##### 유용한 표준 라이브러리 #####
# 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공
import itertools
# 힙 자료구조 제공
import heapq
# 이진 탐색(binary search) 기능 제공
import bisect
# deque, Counter 등의 유용한 자료구조 포함
import collections
# 필수적인 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이 같은 상수 등)
import math



##### 내장 함수 #####
# sum 함수
result = sum([1,2,3,4,5])
print(result)
# 15

# min, max 함수

# eval 함수
result = eval("(3+5)*7")
print(result)
# 56



# sorted()
result = sorted([9,1,8,5,4]) # [1,4,5,8,9]
reverse_result = sorted([9,1,8,5,4], reverse=True) # [9,8,5,4,1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result) # [('홍길동', 35), ('이순신', 75), ('아무개', 50)]

# 순열과 조합
from itertools import combinations_with_replacement, product
data=['A', 'B', 'C']
result1 = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
result2 = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)
#[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# Counter 객체를 활용하여 내부 원소 등장 횟수 구하기
from collections import Counter
counter = Counter(['red','blue','red','green','blue','blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

'''
3
1
{'red': 2, 'blue': 3, 'green': 1}
'''

# 최소공배수(LCM)를 구하는 함수
import math


# 최소 공배수(LCM)를 구하는 함수
def lcm(a,b):
    return a * b // math.gcd(a, b)
a = 21
b = 14
print(math.gcd(a,b))
print(lcm(a,b))
'''
7
42
'''

# 재귀 사용시
import sys
sys.setrecursionlimit(10 ** 6)