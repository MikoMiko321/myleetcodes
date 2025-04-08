# This is O(n) but looks pretty bad
import copy


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        deep_copy = copy.deepcopy(nums)
        i = 0
        while i < len(nums):
            deep_copy[self.get_next_elem_address(nums, i, k)] = nums[i]
            i += 1
        i = 0
        while i < len(nums):
            nums[i] = deep_copy[i]
            i += 1

    def get_next_elem_address(self, nums, current, k):
        if len(nums) - current > k:
            next_elem_address = current + k
        else:
            overflow = k - (len(nums) - current)
            next_elem_address = overflow % len(nums)
        return next_elem_address

# test_array = [1,2,3,4,5,6]
# print(test_array)
# solution = Solution()
# solution.rotate(test_array, 4)
# print(test_array)