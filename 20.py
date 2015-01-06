class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = list()
        for c in s:
            if c==')':
                if len(stack)==0 or stack.pop()!='(':
                    return False
            elif c==']':
                if len(stack)==0 or stack.pop()!='[':
                    return False
            elif c=='}':
                if len(stack)==0 or stack.pop()!='{':
                    return False
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        return False

if __name__=='__main__':
    s = Solution()
    data = ['(', '()', '()[]', '({})', '([]', '']
    for d in data:
        print d,s.isValid(d)