class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if len(s)<=1:
            return 0
        nums = [0 for i in range(len(s))]
        last = [0 for i in range(len(s))]
        last[0] = None
        last_l = None
        for i,c in enumerate(s):
            if c=='(':
                 last[i] = last_l
                 last_l = i
            elif last_l!=None:
                nums[i] = 1
                nums[last_l] = 1
                last_l = last[last_l]
        maxn = 0
        temp = 0
        for i in nums:
            if i!=0:
                temp+=1
            else:
                maxn = max(maxn, temp)
                temp = 0
        maxn = max(maxn, temp)
        return maxn

class Solution3:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        nums = [0 for i in range(len(s))]
        last = None 
        maxn = 0
        for i,c in enumerate(s):
            if c=='(':
                 nums[i] = last
                 last = i
            elif last!=None:
                nums[i] = i-last+1
                j = last-1
                if j>=0 and s[j]==')':
                    nums[i] += nums[j]
                maxn = max(maxn, nums[i])
                last = nums[last]
        return maxn

class Solution2:
    # @param s, a string
    # @return an integer
    # dp solution
    def longestValidParentheses(self, s):
        dp = [0 for i in range(len(s))]
        maxn = 0
        for i in range(1, len(s)):
            if s[i]=='(':
                continue 
            k = dp[i-1]
            j = i-1-k
            if j>=0 and s[j]=='(':
                dp[i] = k+2
                j -= 1
                if j>=0 and dp[j]>0:
                    dp[i] += dp[j]
                maxn = max(maxn, dp[i])
        return maxn

s = Solution()
s2 = Solution2()
s3 = Solution3()

data = [
        '(()', 
        ')()())',
        '()',
        '(((', ')))', '((()', '((()))', '()(()', '())())', '())()(()',
        ''
        ]
# for d in data:
#     print d,s.longestValidParentheses(d)


import time

times = 100

start = time.clock()
for i in range(times):
    for d in data:
        s.longestValidParentheses(d)
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        s2.longestValidParentheses(d)
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        s3.longestValidParentheses(d)
print time.clock()-start
