class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        r = 1
        digits.reverse()
        i = 0
        n = len(digits)
        while r!=0:
            if i>=n:
                digits += [r%10]
                r /= 10
            else:
                temp = digits[i]+r
                digits[i] = temp%10
                r = temp/10
            i += 1
        digits.reverse()
        return digits

s = Solution()
data = [[9,9,9], [0],[8,9,9]]
for d in data:
    print s.plusOne(d)