class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidRow(board,i):
                return False
        
        for j in range(9):
            if not self.isValidColumn(board,j):
                return False   
        for i in range(0, 9, 3):
            for j in range(0,9,3):
                if not self.isValidSubGrid(board, i, j):
                    return False
        return True

    def isValidRow(self, board, row):
        seen = set()
        for i in range(9):
            digit = board[row][i]
            if digit == '.':
                continue
            if digit in seen:
                return False
            seen.add(digit)
        return True

    def isValidColumn(self, board, col):
        seen = set()
        for i in range(9):
            digit = board[i][col]  
            if digit == '.':
                continue
            if digit in seen:
                return False
            seen.add(digit)
        return True
        
    def isValidSubGrid(self, board, row, col):
        seen = set()
        for i in range(row, row+3):
            for j in range(col, col+3):
                digit = board[i][j]
                if digit == '.':
                    continue
                if digit in seen:
                    return False
                seen.add(digit)
        return True