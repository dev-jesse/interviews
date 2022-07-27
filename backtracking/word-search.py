def exist(self, board: List[List[str]], word: str) -> bool:
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if self.bt(board, i, j, word, 0): return True

    return False


def bt(self, board, i, j, word, index):
    if index == len(word): return True
    if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or \
    board[i][j] != word[index]:
        return False

    tmp = board[i][j]
    board[i][j] = "#"
    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if self.bt(board, x, y, word, index + 1): return True
    board[i][j] = tmp

    return False
