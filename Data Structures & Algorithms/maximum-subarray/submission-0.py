class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0
        for num in nums:
            currSum += num
            maxSum = max(currSum, maxSum)
            currSum = max(0, currSum)
        return maxSum