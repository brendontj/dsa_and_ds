class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos_to_visit = set()
        pos_to_ignore = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0 and (r,c) not in pos_to_ignore:
                    for i in range(len(matrix)):
                        if i == r:
                            continue
                        
                        if matrix[i][c] == 0:
                            continue
                        
                        matrix[i][c] = 0
                        pos_to_ignore.add((i, c))
                    
                    for j in range(len(matrix[0])):
                        if j == c:
                            continue
                        
                        if matrix[r][j] == 0:
                            continue
                        
                        matrix[r][j] = 0
                        pos_to_ignore.add((r, j))
