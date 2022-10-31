class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        len_row=len(matrix)
        len_col=len(matrix[0])
        # 这样初始化是不行的 
        # self.presum=[[0]*len_col]*len_row
        self.presum = [[0] * (len_col + 1) for _ in range(len_row + 1)]

        for i in range(len_row):
            for j in range (len_col):
                self.presum[i+1][j+1]=num[i][j]+self.presum[i][j+1]+self.presum[i+1][j]-self.presum[i][j]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1]-self.presum[row2+1][col1]-self.presum[row1][col2+1]+self.presum[row1][col1]

