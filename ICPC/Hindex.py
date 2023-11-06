num = int(input())
nums = []
for _ in range(num):
    nums.append(int(input()))
def check():
    nums.sort(reverse=True)
    total = 0
    for i in range(len(nums)):
        if nums[i] >= i+1:
            total+=1
        else:
            break
    return total
print(check())