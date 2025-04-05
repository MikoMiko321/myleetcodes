class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        last_value = nums[0] - 1
        second = False
        length = len(nums)
        offset = 0
        i = 0
        while i + offset < length:
            if nums[i + offset] > last_value:
                last_value = nums[i + offset]  # Here I wasn't paying attention offset should be used for everything except when we write TO nums[i]
                second = False
                nums[i] = nums[i + offset]
                k += 1
                i += 1
            else:
                if not second:
                    second = True
                    nums[i] = nums[i + offset]
                    k += 1
                    i += 1
                else:
                    offset += 1
        return k


solution = Solution()
input_nums = [1,1,1,2,2,2,3,3]
print(input_nums)
print(solution.removeDuplicates(input_nums), input_nums)
