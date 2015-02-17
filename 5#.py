class Solution:
    # @return a string
    # Manacher's ALGORITHM
    def longestPalindrome(self, s):
        ns = '$'
        for c in s:
            ns += '#'+c
        ns += '#'
        p = [1]*len(ns)
        index = 0
        mx = 0
        max_id = 0
        max_len = 0
        for i in range(1, len(ns)):
            if mx>i:
                p[i] = min(p[2*index-i], mx-i)
            while (i+p[i])<len(ns) and ns[i+p[i]]==ns[i-p[i]]:
                p[i] += 1
            if i+p[i]>mx:
                mx = i+p[i]
                index = i
            if p[i]>max_len:
                max_id = i
                max_len = p[i]
        ans = ''
        for i in range(max_id-max_len+2, max_id+max_len-1, 2):
            ans += ns[i]
        return ans

if __name__=='__main__':
    s = Solution()
    data = ['aba', 'abb', 'bbb', 'a','12321']
    for d in data:
        print d,s.longestPalindrome(d)