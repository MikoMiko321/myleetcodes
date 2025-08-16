# O(N**2)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):   
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        delta = [gas[i] - cost[i] for i in range(len(gas))]
        if len(gas) == 1 and sum(delta) >= 0:
            return 0
        if sum(delta) < 0:
            return -1
        if delta[len(gas)-1]:
            after_negative = True
        else:
            after_negative = False
        for i in range(len(gas)):
            if delta[i] < 0:
                after_negative = True
            if delta[i] >= 0 and after_negative == True:
                after_negative = False
                temp_sum = 0
                for j in range(len(gas)):
                    fail = False
                    temp_sum += delta[(i+j) % len(gas)]
                    if temp_sum < 0:
                        fail = True
                        break
                if fail == False:
                    return i
        return -1  

mysolution = Solution()
print(mysolution.canCompleteCircuit([2,3,4], [3,4,3]))