class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_sequence = 0
        for num in nums:
            local_max = 1
            if num - 1 not in s:
                aux = num
                while aux + 1 in s:
                    aux += 1
                    local_max += 1
                if local_max > max_sequence:
                    max_sequence = local_max
        return max_sequence

