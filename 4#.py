class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1, self.nums2 = nums1, nums2
        self.len1, self.len2 = len(nums1), len(nums2)
        total = self.len1 + self.len2
        if total & 1 == 0:
            return (self.find(0, 0, total/2)+
                self.find(0, 0, total/2+1))/2.0
        else:
            return self.find(0, 0, total/2+1)
        
    def find(self, s1, s2, k):
        # print s1,s2,k
        if s1 >= self.len1:
            return self.nums2[s2+k-1]
        if s2 >= self.len2:
            return self.nums1[s1+k-1]
        if k == 1:
            return min(self.nums1[s1], self.nums2[s2])

        sa = self.nums1[s1+k/2-1] if s1+k/2-1 < self.len1 else None 
        sb = self.nums2[s2+k/2-1] if s2+k/2-1 < self.len2 else None 

        if (sa is None or sa > sb) and sb is not None:
            return self.find(s1, s2+k/2, k-k/2)
        return self.find(s1+k/2, s2, k-k/2)


data = ([1,3,5],[2,4])
data = ([1], [2,3,4,5,6])
# data = ([1,2], [1,2])
data = ([2,3,4,5,6], [1])
print Solution().findMedianSortedArrays(data[0], data[1])