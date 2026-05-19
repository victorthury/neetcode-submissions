class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        
        longest = 0
        for num in nums:
            if num - 1 not in s:
                curr = 1
                while num + 1 in s:
                    curr += 1
                    num += 1
                if curr > longest:
                    longest = curr
        return longest