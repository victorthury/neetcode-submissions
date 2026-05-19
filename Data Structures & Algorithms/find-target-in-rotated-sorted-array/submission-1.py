class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMin():
            l = 0
            r = len(nums) - 1

            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return r
        
        l = 0
        r = len(nums) - 1

        if nums[l] > nums[r]:
            minPos = findMin()
            if target > nums[r]:
                r = minPos - 1
            else:
                l = minPos
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return -1

