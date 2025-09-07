# O(n) worst solution possible
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1] * len(ratings)
        advantage_map = []
        # create advantage map and place initial ammount of candy
        for i in range(len(ratings)):
            if (i > 0 and ratings[i] > ratings[i - 1]) or (
                i + 1 < len(ratings) and ratings[i] > ratings[i + 1]
            ):  # Advantage condition
                advantage_map.append(1)
            else:
                advantage_map.append(0)
            if i > 0:
                if ratings[i] > ratings[i - 1]:
                    candy[i] = candy[i - 1] + 1
                elif ratings[i] < ratings[i - 1]:
                    candy[i] = candy[i - 1] - 1
                else:
                    candy[i] = candy[i - 1]
        inside_advantege_interval = False
        advantage_interval = []
        final_result = []
        # fix advantage intervals on min value and set disadvantage to 1
        for i in range(len(ratings)):
            if advantage_map[i] == 0 or i == len(ratings) - 1:
                if inside_advantege_interval == True:
                    # fix on min value
                    diff = 2 - min(advantage_interval)
                    for j in range(len(advantage_interval)):
                        advantage_interval[j] += diff
                    final_result.extend(advantage_interval)
                    inside_advantege_interval = False
                    advantage_interval = []
                if advantage_map[i] == 0:
                    final_result.append(1)
                else:
                    final_result.append(final_result[len(final_result) - 1] + 1)
            else:
                inside_advantege_interval = True
                advantage_interval.append(candy[i])
        # minimize advantage values
        if len(ratings) >= 3:
            for i in range(1, len(ratings) - 1):
                if final_result[i - 1] < final_result[i] <= final_result[i + 1]:
                    final_result[i] = final_result[i - 1] + 1
            for i in range(len(ratings) - 2, 0, -1):
                if final_result[i - 1] >= final_result[i] > final_result[i + 1]:
                    final_result[i] = final_result[i + 1] + 1

        print(advantage_map)
        print(candy)
        print(final_result)
        return sum(final_result)


mysolution = Solution()
arr = [1, 0, 2]
# [1,6,10,8,7,3,2]
# [1,2,87,87,87,2,1]
# name: str = "Peter"

print(mysolution.candy(arr))
