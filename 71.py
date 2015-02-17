class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        dirs = []
        i = 0
        n = len(path)
        while i<n:
            j = i+1
            while j<n and path[j]!='/':
                j += 1
            name = path[i+1:j]
            if name=='..':
                if len(dirs)>0:
                    dirs.pop()
            elif name!='' and name!='.':
                dirs.append(name)
            i = j
        return '/'+'/'.join(dirs)

class Solution2:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        dirs = []
        for d in path.split("/"):
            if d in ('', '.', '/'):
                continue
            if d == '..':
                dirs = dirs[:-1]
            else:
                dirs.append(d)
        return '/' + '/'.join(dirs)

s = Solution()
s2 = Solution2()
data = [
    '/home/', 
    '/a/./b/../../c/', 
    '/../', '/home//foo/', '/home',
    ''
    ]


import time
times = 100

start = time.clock()
for i in range(times):
    for d in data:
        s.simplifyPath(d)
print time.clock()-start

start = time.clock()
for i in range(times):
    for d in data:
        s2.simplifyPath(d)
print time.clock()-start