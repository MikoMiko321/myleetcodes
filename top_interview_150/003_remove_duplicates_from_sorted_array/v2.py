class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        Код выглядит лаконичнее и красивее, но скорость все таже! Возможно, можно пропустить несколько итераций, зная наибольшее значение изначально!
        Если с самого начала делать эту проверку, то отсортируем быстрее, но не посчитаем всех повторов!
        Как определить ситуацию когда [x x x x x MAX MAX ... MAX]

        Complexity: O(N)

        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
        The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

        Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
        The remaining elements of nums are not important as well as the size of nums. Return k.
        """
        dupes_total = 0  # Total number of duplicates
        i = 0
        while i + dupes_total + 1 < len(nums) and (
            nums[i] < nums[len(nums) - 1]
            or nums[i + dupes_total] == nums[len(nums) - 1]
        ):  # While we have NEXT element available and current ellement is less than the greatest
            if (
                nums[i + dupes_total + 1] > nums[i]
            ):  # If next number after known dupes is GREATER than current
                nums[i + 1] = nums[
                    i + dupes_total + 1
                ]  # Write next greater number to absolute next number
                i += 1  # go to absolute next
            else:
                dupes_total += 1  # Skip dupe
        print(nums, len(nums) - dupes_total)
        return (
            len(nums) - dupes_total
        )  # Число уникальных элементов выразим как элементов всего - повторов => повторы = всего - уникальные


solution = Solution()
solution.removeDuplicates([-1, 0, 0, 0, 0, 3, 3])
