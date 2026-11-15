class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr != ".":
                    boxPos = (r//3)*3 + (c//3)
                    if curr in rows[r] or curr in cols[c] or curr in boxes[boxPos]:
                        return False
                    
                    rows[r].add(curr)
                    cols[c].add(curr)
                    boxes[boxPos].add(curr)
        
        return True


        