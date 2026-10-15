class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sqs = {}

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x != '.':
                    if (x in rows.get(r, set())
                     or x in cols.get(c, set()) 
                     or x in sqs.get((r//3, c//3), set())):
                        return False
                    else:
                        rows.setdefault(r, set()).add(x)
                        cols.setdefault(c, set()).add(x)
                        sqs.setdefault((r//3, c//3), set()).add(x)

        return True