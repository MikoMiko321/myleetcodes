class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        obstacle_zero_at = None
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0 and i != len(nums) - 1 and obstacle_zero_at is None:  # I forgot to include the last condition even though I've realized that its necessary.
                obstacle_zero_at = i
            if obstacle_zero_at is not None:
                if nums[i] > obstacle_zero_at - i:
                    obstacle_zero_at = None
        if obstacle_zero_at is None:
            return True
        else:
            return False
