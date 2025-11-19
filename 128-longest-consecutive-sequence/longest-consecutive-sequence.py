class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        count = 0
        last_smaller = float("-inf")
        longest = 0

        for i in range(0,n):
            num = nums[i]
            if num - 1 == last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num
            longest = max(longest, count)
        return longest