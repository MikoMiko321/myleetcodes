class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Я понял, что эта задача решается в 3 строчки, НО в данном случае, не выполняется условие in-place!!
        Complexity: O(N)

        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
        The remaining elements of nums are not important as well as the size of nums. Return k.
        """
        unique_set = set(nums)
        nums = list(unique_set)
        return len(unique_set)  # Число уникальных элементов выразим как элементов всего - повторов => повторы = всего - уникальные


solution = Solution()
solution.removeDuplicates([1,1,2])
