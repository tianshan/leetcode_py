class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens, lenp = len(s), len(p)
        i, j = 0, 0
        last_i, last_j = -1, -1
        while i<lens:
            if j<lenp and p[j]=='*':
                last_i, last_j = i, j
                i -= 1
            elif j<lenp and s[i]!=p[j] and p[j]!='?':
                if last_i!=-1:
                    i, j = last_i, last_j
                    last_i = last_i+1
                else:
                    return False
            elif j==lenp and last_i!=-1:
                i, j = last_i, last_j
                last_i = last_i+1
            i,j = i+1, j+1

        while j<lenp and p[j]=='*': j += 1
        return i==lens and j == lenp


data = [
    # ["aa","a"],
    # ["aa","aa"],
    # ["aaa","aa"],
    # ["aa", "*"],
    # ["aa", "a*"],
    # ["ab", "?*"],
    # ["aab", "c*a*b"],
    ["aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"],
    ["abbbaaaaaaaabbbabaaabbabbbaabaabbbbaabaabbabaabbabbaabbbaabaabbabaabaabbbbaabbbaabaaababbbbabaaababbaaa", 
    "ab**b*bb*ab**ab***b*abaa**b*a*aaa**bba*aa*a*abb*a*a"]
    ]

for d in data:
    print d, Solution().isMatch(d[0], d[1])
