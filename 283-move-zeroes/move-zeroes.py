class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 0:
            return nums
    
        i = 0
        while i < n and nums[i] != 0:
            i += 1
    
        if i == n:     #  it will if all element are sorted then return 
            return nums
    

        j = i + 1

        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        return nums