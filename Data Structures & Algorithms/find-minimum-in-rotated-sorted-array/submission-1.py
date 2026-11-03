class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        middle = (l + r) // 2

        while r > l:
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle
            middle = (l + r) // 2
        return nums[middle]