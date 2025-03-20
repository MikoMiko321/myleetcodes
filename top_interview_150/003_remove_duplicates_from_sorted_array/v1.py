class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Complexity: O(N)
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
        The remaining elements of nums are not important as well as the size of nums. Return k.
        """
        k_value = len(nums) - 0  # Число уникальных элементов выразим как элементов всего - повторов => повторы = всего - уникальные
        duplicate_number = None  # Current number that we consider duplicate
        i = 0
        while i + len(nums) - k_value + 1 < len(nums):  # While we have NEXT element available
            if nums[i + len(nums) - k_value] == nums[i + len(nums) - k_value + 1]:  # If next number is duplicate
                duplicate_number = nums[i + len(nums) - k_value]
                # Ниже важен порядок проверки! Сперва мы проверяем, что не выходим
                # за рамки массива и только потом - элементы этого самого массива.
                while i + len(nums) - k_value + 1 < len(nums) and nums[i + len(nums) - k_value + 1] == duplicate_number:
                    k_value -= 1
                if i + len(nums) - k_value + 1 >= len(nums):
                    return k_value
                else:
                    nums[i + 1] = nums[i + len(nums) - k_value + 1]  # We write unique to the first duplicate in the next slot
                    i += 1
            else:
                nums[i + 1] = nums[i + len(nums) - k_value + 1]
                i += 1
        return k_value


solution = Solution()
solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
