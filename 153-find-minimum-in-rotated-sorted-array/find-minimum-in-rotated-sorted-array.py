class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        minimum = nums[0]
        for x in nums:
            if x < minimum:
                minimum = x
        return minimum
    