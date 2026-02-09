from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1
        prev_num = nums[0]

        for n in nums[1:]:
            if n != prev_num:
                prev_num = n
                nums[k] = n
                k += 1

        return k


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3]

    result = sol.removeDuplicates(nums)
    print(result)          # 3
    print(nums[:result])   # [1, 2, 3]
