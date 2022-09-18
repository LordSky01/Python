nums = [10,2,3,4]
result = []


p = 1

for i in range(0,len(nums)):
    result.append(p)
    p = p * nums[i]

p =1

for i in range(len(nums)-1, -1, -1):
    result[i] = result[i] * p
    p = p* nums[i]

print(result)

