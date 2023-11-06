num = int(input())
total = 0
for _ in range(num):
    x, y = list(map(float, input().split()))
    total += x*y
print(total)