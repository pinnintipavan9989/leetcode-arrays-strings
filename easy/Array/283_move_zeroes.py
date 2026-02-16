def isMoveZero(nums):
    p1,p2 = 0,0
    while (p1<len(nums)):
        if nums[p1] != 0:
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp

            p2 += 1
        p1 += 1
    return nums
r1 = [0,1,0,3,12]
print(isMoveZero(r1))
print(isMoveZero([1,0,3,12]))