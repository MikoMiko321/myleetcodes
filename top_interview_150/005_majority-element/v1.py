# This is time complexity O(n^2) solution but space complexity O(1)
from os import supports_dir_fd


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dummy = 1000000001
        counter = 0
        i = 0
        while i < len(nums):
            if nums[
                i] != dummy:  # lesson to learn: "==" checks if values are equal, "is" checks if objects are the same (i.e., same memory address).
                current_element = nums[i]
                j = i
                while j < len(nums):
                    if nums[j] == current_element:
                        counter += 1
                        nums[j] = dummy
                    j += 1
                if counter > len(nums) / 2:
                    return current_element
                i += 1
            else:
                i += 1


solution = Solution()
test_subject = [1000, 2, 1001, 1000, 1000]
print(test_subject)
print(solution.majorityElement(test_subject))
