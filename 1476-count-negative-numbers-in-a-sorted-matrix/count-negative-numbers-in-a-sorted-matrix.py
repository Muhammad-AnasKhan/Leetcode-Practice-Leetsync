class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # brute force
        # count = 0
        # for i in grid:
        #     for j in i:
        #         if j < 0:
        #             count += 1
        # return count

        #  visualizing the matrix
        # [4, 3,  2, -1]
        # [3, 2,  1, -1]
        # [1, 1, -1, -2]
        # [-1,-1,-2, -3]

        # optimal solution
        # the idea is to start from the bottom left of the matrix
        # and keep track of the count of negative numbers
        # as the matrix is sorted in descending order, both rows and col wise
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        curr_row = rows - 1
        curr_col = 0

        while(curr_row >= 0 and curr_col < cols):
            if grid[curr_row][curr_col] < 0:
                count += cols - curr_col
                curr_row -= 1
            else:
                curr_col += 1
        
        return count