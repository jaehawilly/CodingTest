n = int(input())
change = 1000-n
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in range(6):
    cnt += change//money[i]
    change = change % money[i]
print(cnt)
