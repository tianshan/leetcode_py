class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.rows = [[str(i) for i in range(1,10)] for j in range(1,10)]
        self.cols = [[str(i) for i in range(1,10)] for j in range(1,10)]
        self.boxs = [[str(i) for i in range(1,10)] for j in range(1,10)]

        new_board = self.init(board)
        self.dfs(new_board, 0, 0)
        for i in range(9):
            board[i] = ''.join(new_board[i])

    def init(self, board):
        new_board = []
        for i in range(9):
            new_board.append([])
            for j in range(9):
                if board[i][j]!='.':
                    self.remove(board[i][j], i, j)
                new_board[-1].append(board[i][j])
        return new_board

    def remove(self, num, i, j):
        try:
            self.rows[i].remove(num)
        except:
            pass
        try:
            self.cols[j].remove(num)
        except:
            pass
        try:
            self.boxs[i/3*3+j/3].remove(num)
        except:
            pass

    def append(self, num, i, j):
        self.rows[i].append(num)
        self.cols[j].append(num)
        self.boxs[i/3*3+j/3].append(num)

    def dfs(self, board, i, j):
        if j>=9:
            return self.dfs(board, i+1, 0)
        if i>=9:
            return True
        if board[i][j]!='.':
            return self.dfs(board, i, j+1)

        candi = set(self.rows[i]) & set(self.cols[j]) & set(self.boxs[i/3*3+j/3])
        for x in candi:
            board[i][j] = x 
            self.remove(x, i, j)
            res = self.dfs(board, i, j+1)
            if res:
                return True
            self.append(x, i, j)
            board[i][j] = '.'
        return False


def print_board(board):
    for d in board:
        print d
    print ''

s = Solution()

data = ['53..7....',
        '6..195...',
        '.98....6.',
        '8...6...3',
        '4..8.3..1',
        '7...2...6',
        '.6....28.',
        '...419..5',
        '....8..79']

print_board(data)

s.solveSudoku(data)
print_board(data)