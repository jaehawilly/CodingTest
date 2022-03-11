import sys
si = sys.stdin.readline
n = int(si().rstrip())  # n을 int로 변환
s = []
for i in range(n):
    first, second = map(int, si().rstrip().split())
    s.append([first, second])
# 시작시간(first)을 기준으로 먼저 정렬
s = sorted(s, key=lambda a: a[0])
# 종료시간(second)을 기준으로 다시 한번 정렬
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:  # last보다 큰 시작시간이 나오면
        cnt += 1  # cnt 1 증가
        last = j  # last 갱신
print(cnt)
