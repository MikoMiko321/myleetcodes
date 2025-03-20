class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp_list = []
        for i in range(m):
            temp_list.append(nums1[i])
        i = 0
        j = 0
        k = 0
        while i < m or j < n:
            if i >= m:
                nums1[k] = nums2[j]
                k += 1
                j += 1
            elif j >= n:
                nums1[k] = temp_list[i]
                i += 1
                k += 1
            else:
                if temp_list[i] < nums2[j]:
                    nums1[k] = temp_list[i]
                    i += 1
                    k += 1
                elif temp_list[i] == nums2[j]:
                    nums1[k] = temp_list[i]
                    i += 1
                    k += 1
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1
                else:
                    nums1[k] = nums2[j]
                    k += 1
                    j += 1


solution = Solution()
solution.merge([1], 1, [], 0)
