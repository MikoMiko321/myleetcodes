# This is considered O(n), I wonder why, got to figure at some point...
import math


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        This uses eliminate the impossible approach, can be optimized by doing a single manual pass to calculate
        theoretical_h_index_maximum, but practice shows, that we get a memory effective solution by using
        max() and sum() and much less code lines.
        """
        # total_value = 0
        # maximum_value = 0
        # for j in range(len(citations)):
        #     if citations[j] > maximum_value:
        #         maximum_value = citations[j]
        #     maximum_value += citations[j]
        theoretical_h_index_maximum = int(
            min(
                max(citations),
                len(citations),
                math.floor(math.sqrt(sum(citations))),
            )
        )
        # theoretical_h_index_maximum = int(min(maximum_value, len(citations), math.floor(math.sqrt(total_value))))
        for i in range(theoretical_h_index_maximum, 0, -1):
            i_count = 0
            for j in range(len(citations)):
                if citations[j] >= i:
                    i_count += 1
                if i_count >= i:
                    return i
        return theoretical_h_index_maximum
