class Solution:
    # @return a boolean
    def isPalindrome1(self, x):
        if x<0:
            return False
        if x<10:
            return True
        x_len = 0
        temp = x 
        while temp!=0:
            x_len += 1
            temp /= 10
        x_len_2 = x_len / 2
        r = 0 
        for i in range(x_len_2):
            r = r*10+x%10
            x /= 10

        if x_len&1==1:
            x /= 10
        if x==r:
            return True
        return False

    def isPalindrome2(self, x):
        if x<0:
            return False
        x = str(x)
        x_len = len(x)/2
        for i in range(x_len):
            if x[i]!=x[-(i+1)]:
                return False
        return True

    def isPalindrome(self, x):
        x = str(x)
        return x==x[::-1]

if __name__=="__main__":
    import time
    data = [1,2,11,101,12321,1221,1212, 12312, -1, 1234567899, 10]*1000
    s = Solution()
    start = time.clock()
    for d in data:
        # print d,s.isPalindrome(d)
        s.isPalindrome(d)
    end = time.clock()
    print end-start
    start=end
    for d in data:
        # print d,s.isPalindrome1(d)
        s.isPalindrome1(d)
    end = time.clock()
    print end-start
    start=end
    for d in data:
        # print d,s.isPalindrome2(d)
        s.isPalindrome2(d)
    end = time.clock()
    print end-start
    start=end