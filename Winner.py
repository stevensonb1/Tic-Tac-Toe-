def win_indexes(n):
    for r in range(n):
        yield [(r, c) for c in range(n)]
    for c in range(n):
        yield [(r, c) for r in range(n)]
    yield [(i, i) for i in range(n)]
    yield [(i, n - 1 - i) for i in range(n)]


def is_winner(board, decorator):
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[r][c] == decorator for r, c in indexes):
            return True
    return False