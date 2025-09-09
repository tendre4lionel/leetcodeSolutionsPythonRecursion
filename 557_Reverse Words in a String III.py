# 557 Reverse Words in a String III
# Algorithm:
# - Split the string into words using spaces
# - Reverse each word individually
# - Join the words back with spaces
# Complexity:
# - Time: O(n), n = length of string
# - Space: O(n), for storing the reversed words

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reversed_words = []
        
        for word in words:
            reversed_words.append(word[::-1])
        
        return ' '.join(reversed_words)

# Example usage:
# sol = Solution()
# print(sol.reverseWords("Let's take LeetCode contest"))
# Output: "s'teL ekat edoCteeL tsetnoc"










