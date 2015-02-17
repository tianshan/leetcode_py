class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n_len = len(num)
        if n_len<=1:
            return num
        last = num[-1]
        for i in range(2, n_len+1):
            if num[-i]<last:
                break
            last = num[-i]

        i = n_len-i
        temp = num[i]
        if temp>=num[i+1]:
            self.invertOrder(num, 0, n_len-1)
            return num
        for j in range(i+1, n_len):
            if num[j]<=temp:
                break
        if num[j]<=temp:
            j = j-1
        # print i,j
        num[i] = num[j]
        num[j] = temp
        self.invertOrder(num, i+1, n_len-1)
        return num

    def invertOrder(self, num, i, j):
        while i<j:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
            i += 1
            j -= 1

if __name__=="__main__":
    s = Solution()
    data = [
            [1,2,3],[3,2,1],[1,1,5],
            [1,2,3,4],[1,4,3,2],[1,2,4,3],[1,4,2,3],[1,3,2,4],[1,3,4,2],
            [1,5,1],[5,1,1],
            [1,1,2,2,5],[1,1,5,2,2],
            [2,2,7,5,4,3,2,2,1]
            ]
    for d in data:
        print d,
        s.nextPermutation(d)
        print d