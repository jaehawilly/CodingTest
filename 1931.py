n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 0
for i in range(n):
    r = 0
    for j in range(i+1):
        r += a[j]
    result += r
print(result)