class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        this is docstring
        """
        k_value = 0
        i = 0
        while i + k_value < len(nums):
            if nums[i + k_value] == val:
                # Ниже важен порядок проверки! Сперва мы проверяем, что не выходим
                # за рамки массива и только потом - элементы этого самого массива.
                while i + k_value < len(nums) and nums[i + k_value] == val:
                    k_value += 1
                if i + k_value >= len(nums):
                    return len(nums) - k_value
                else:
                    nums[i] = nums[i + k_value]
                    i += 1
            else:
                nums[i] = nums[i + k_value]
                i += 1
        return len(nums) - k_value  # Здесь я был невнимателен к условию задачи


solution = Solution()
solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
