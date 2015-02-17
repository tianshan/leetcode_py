
def findPeakElement(num):
    if len(num)==1:
        return 0
    for i,k in enumerate(num):
        if i==0 and len(num):
            if num[i]>num[i+1]:
                return i
        if i==len(num)-1:
            if num[i]>num[i-1]:
                return i
        if num[i]>num[i-1] and num[i]>num[i+1]:
            return i

if __name__=="__main__":
    num = [1,2]
    print findPeakElement(num)