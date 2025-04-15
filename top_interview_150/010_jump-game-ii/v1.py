# O(n^2) solution, create shadow list and measure it, there should be a better way
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        shadows = [None]*(len(nums)-1)
        for i in range(len(nums)-2, -1, -1):
            if nums[i]>len(nums)-1-i:  # If number of jumps goes outside set it to go to last
                shadow_len = len(nums)-1-i
            else:
                shadow_len = nums[i]
            # overshadow only if goes same destination or further
            for j in range(shadow_len):
                if i+shadow_len<=len(shadows)-1 and shadows[i+j] == shadows[i+shadow_len]: # check if there is an element outside shadow and if that element is the same as the one we want to overwrite - we do nothing
                    pass
                else:
                    shadows[i+j] = i
        return len(set(shadows))


test_array = [1,1]
print(test_array)
solution = Solution()
print(solution.jump(test_array))
