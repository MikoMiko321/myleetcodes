# Time Complexity:
# O(N² × U)
# Where N is the length of nums, and U is the number of unique elements.
# Space Complexity:
# O(U)
# Where U is the number of unique elements.
# Mistakes:
# 1 conceptual big mistake, my initial formula didn't take into account fact that subarray should be unbreakable
# 2 small mistakes in code logic

class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum_complete_subarray = {num: 0 for num in nums}
        print(minimum_complete_subarray)
        complete_subarrays = 0
        tail = 0
        old_tail = 0
        head = 0
        while head < len(nums):
            while True:
                minimum_complete_subarray[nums[head]] += 1
                if min(minimum_complete_subarray.values()) < 1:
                    head += 1  # should increase head only if min(minimum_complete_subarray.values()) < 1
                else:
                    break
                if head == len(nums):
                    return complete_subarrays
            while tail < len(nums):
                if minimum_complete_subarray[nums[tail]] > 1:
                    minimum_complete_subarray[nums[tail]] -= 1  # I was modifying tail before changing current value
                    tail += 1
                else:
                    break
            complete_subarrays += (1 + tail - old_tail) * (len(nums) - head)
            minimum_complete_subarray = {num: 0 for num in nums}
            tail += 1
            old_tail = tail
            head = tail
        return complete_subarrays


solution = Solution()
print(solution.countCompleteSubarrays([1641, 448, 1641, 1437, 448, 1406, 1437]))
