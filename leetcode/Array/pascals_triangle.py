class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        numElements = 1
        for row in range (0, numRows):
            rows.append([])
            for idx in range(numElements):
                if idx == 0 or idx == numElements -1:
                    rows[row].append(1)
                else:
                    rows[row].append(rows[row-1][idx] +  rows[row-1][idx-1])
            numElements += 1
        return rows
