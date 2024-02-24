class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        min_len = min(len1, len2)

        for i in range(min_len, 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                delitelj = str1[:i]
                if str1 == delitelj * (len1 // i) and str2 == delitelj * (len2 // i):
                    return delitelj
        return ""
