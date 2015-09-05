class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        if len1 == 0 or len2 == 0:
            return len1 or len2
        ans = [[0 for i in range(len2)] for j in range(len1)]
        for i in xrange(len1):
            for j in xrange(len2):
                if word1[i] == word2[j]:
                    if i==0 and j==0: ans[i][j] = 0
                    elif i==0: ans[i][j] = j
                    elif j==0: ans[i][j] = i
                    else: ans[i][j] = ans[i-1][j-1]
                else:
                    if i==0 and j==0: ans[i][j] = 1
                    elif i==0: ans[i][j] = ans[i][j-1] + 1
                    elif j==0: ans[i][j] = ans[i-1][j] + 1
                    else:
                        ans[i][j] = 1+min(ans[i][j-1], ans[i-1][j], ans[i-1][j-1])
        # print "  "+" ".join(word2)
        # for i in xrange(len1):
        #     print word1[i],
        #     for j in xrange(len2):
        #         print ans[i][j],
        #     print ''
        return ans[len1-1][len2-1]

class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """      
        len1, len2 = len(word1), len(word2)
        if len1 == 0 or len2 == 0:
            return len1 or len2
        ans = range(len2+1)
        for i in range(1, len1+1):
            pre = ans[0]
            ans[0] = i
            for j in range(1, len2+1):
                tmp = ans[j]
                if word1[i-1] == word2[j-1]:
                    ans[j] = pre
                else:
                    ans[j] = 1+min(pre, ans[j], ans[j-1])
                pre = tmp
        return ans[len2]


data = [
    ("abc","adc"), 
    # ("ac", "cd"), 
    # ("",""), 
    # ("","a"),
    # ("sea", "ate"),
    # ("a","ab")
    ]

for d in data:
    # print Solution().minDistance(d[0], d[1]), 
    print Solution2().minDistance(d[0], d[1])
