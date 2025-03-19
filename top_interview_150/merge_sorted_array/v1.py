class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp_list = []
        for i in range(m):
            temp_list.append(nums1[i])
        print(temp_list)

        # i = 0
        # j = 0
        # while


solution = Solution()
solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
