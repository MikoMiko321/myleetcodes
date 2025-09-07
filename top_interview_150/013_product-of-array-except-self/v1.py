# O(N) Solution
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_product = None
        answer = None
        zeroes = [0, 0]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes[0] += 1
                if zeroes[0] == 2:
                    answer = [0] * len(nums)
                    return answer
                zeroes[1] = i
                continue
            print(zeroes)
            if total_product is None:
                total_product = nums[i]
                continue
            total_product *= nums[i]
        print(zeroes)
        if zeroes[0] == 1:
            answer = [
                total_product if i == zeroes[1] else 0 for i in range(len(nums))
            ]
            return answer
        answer = [total_product // nums[i] for i in range(len(nums))]
        return answer


mysoultion = Solution()
print(mysoultion.productExceptSelf([0, 1, 0, -3, 0]))
