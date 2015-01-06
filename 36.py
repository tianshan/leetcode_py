class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        if len(board)!=9:
            return False
        cols = [[] for i in range(9)]
        boxs = [[] for i in range(9)]

        for i in range(9):
            if len(board[i])!=9:
                return False
            a = list()
            for j in range(9):
                x = board[i][j]
                if x=='.':
                    continue
                if x<'1' or x>'9':
                    return False
                a.append(x)
                cols[j].append(x)
                index = (i/3)*3+(j/3)
                boxs[index].append(x)
            if len(set(a))!=len(a):
                return False
        for i in range(9):
            if len(boxs[i])!=len(set(boxs[i])):
                return False
            if len(cols[i])!=len(set(cols[i])):
                return False
        return True

if __name__=='__main__':
    s = Solution()
    data = ['53..7....',
            '6..195...',
            '.98....6.',
            '5...6...3',
            '4..8.3..1',
            '7...2...6',
            '.6....28.',
            '...419..5',
            '....8..79']
    print s.isValidSudoku(data)
