import math
from collections import Counter

n, d = list(map(int, input().split()))
inputs = list(map(int, input().split()))

index = [math.floor(i/d) for i in inputs]

counter = Counter(index)

pairs = sum(v*(v-1)//2 for v in counter.values())

print(pairs)
