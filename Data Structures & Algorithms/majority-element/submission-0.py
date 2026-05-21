class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        maxCount = 0

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

            if hashmap[num] > maxCount:
                maxCount = hashmap[num]
                res = num
        return res