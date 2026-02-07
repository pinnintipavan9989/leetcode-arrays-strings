def twoSum(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        rem = target - n
        if rem in seen:
            return [seen[rem], i]
        seen[n] = i

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))