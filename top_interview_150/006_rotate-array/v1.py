# This is a draft solution, which isn't working now

class Solution(object):
    precession_activated = False
    precession = 0
    first_value = True
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 2 and k != 0 and len(nums) % k == 0:
            self.precession = 1
        else:
            self.precession = 0
        i = 0
        elem_address = 0
        saved_value_old = nums[elem_address]
        elem_address = self.get_next_elem_address(nums, elem_address, k)
        self.precession_activated = False
        while i < len(nums):
            if self.precession_activated:
                saved_value_new = nums[elem_address + self.precession]
                nums[elem_address] = saved_value_old
                elem_address += self.precession
                self.precession_activated = False
            else:
                saved_value_new = nums[elem_address]
                nums[elem_address] = saved_value_old
                if self.first_value:
                    nums[0] = nums[-k]
                    self.first_value = False

            elem_address = self.get_next_elem_address(nums, elem_address, k)
            saved_value_old = saved_value_new
            i += 1

    def get_next_elem_address(self, nums, current, k):
        if len(nums) - current > k:
            next_elem_address = current + k
        else:
            overflow = k - (len(nums) - current)
            next_elem_address = overflow % len(nums)
            if self.precession == 1:
                self.precession_activated = True
        return next_elem_address

test_array = [1,2,3,4,5,6]
print(test_array)
solution = Solution()
solution.rotate(test_array, 4)
print(test_array)