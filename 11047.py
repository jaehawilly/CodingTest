from audioop import reverse


n, k = map(int, input().split())
coin_lst = []
for i in range(n):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(n)):  # 내림차순으로 바꿈
    count += k//coin_lst[i]  # count에 나머지 더해서 업데이트
    k = k % coin_lst[i]  # k를 업데이트

print(count)
