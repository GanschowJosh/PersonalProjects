n, k = list(map(int, input().split()))

pointDict = {}
for i in range(n):
    x, y = list(map(float,input().split()))
    pointDict[i] = (x, y)

area = 0.0
for j in range(k):
    if j != k-1:
        area += ((pointDict[j][0]*pointDict[j+1][1]) - (pointDict[j][1]*pointDict[j+1][0]))
    else:
        area += ((pointDict[j][0]*pointDict[0][1]) - (pointDict[j][1]*pointDict[0][0]))

print(0.5*abs(area))