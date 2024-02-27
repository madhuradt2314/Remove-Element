class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0  
        k = 0  
        while i < len(nums):
            if nums[i] != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            i += 1
        return k
