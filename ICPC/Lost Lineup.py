num = int(input())
dists = list(map(int, input().split()))
order = [1]
for i in range(num-1):
    order.append(dists.index(i)+2)
for i in range(len(order)):
    print(order[i], end=" ")