n = int(input())
bag = 0
while n >= 0:
    if n % 5 == 0:  # 5의 배수라면
        bag += (n//5)  # 5킬로 봉지 개수 +1
        print(bag)
        break
    n -= 3  # 3으로 계속 빼줄때마다
    bag += 1  # 3킬로 봉지 개수 +1
else:  # 정확히 만들 수 없다면
    print(-1)  # -1 출력
