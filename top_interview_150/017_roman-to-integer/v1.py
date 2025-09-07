class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        my_dict = {
            "I": (0, 1),
            "V": (1, 5),
            "X": (2, 10),
            "L": (3, 50),
            "C": (4, 100),
            "D": (5, 500),
            "M": (6, 1000),
        }
        r_value = 0
        last_char = "I"
        for char in reversed(s):
            if my_dict[char][0] < my_dict[last_char][0]:
                r_value -= my_dict[char][1]
            else:
                r_value += my_dict[char][1]
            last_char = char
        return r_value


mysolution = Solution()
print(mysolution.romanToInt("MCMXCIV"))
