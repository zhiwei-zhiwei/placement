def check_win(board, r, c, n, disc):
    # Check horizontal, vertical, and both diagonal directions
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for dr, dc in directions:
        count = 0
        for i in range(n):
            # Calculate the row and column indices
            nr, nc = r + i * dr, c + i * dc

            # If out of bounds, break
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == disc:
                count += 1
            else:
                break

            # If count reaches n, return True
            if count == n:
                return True
    return False


def connect_n_win():
    # Read board dimensions and connection amount
    rows, cols, n = map(int, input().split())

    # Read board
    board = [input().split() for _ in range(rows)]
    print(board)
    # Check for red and blue wins
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R' and check_win(board, i, j, n, 'R'):
                return 'RED WINS'
            elif board[i][j] == 'B' and check_win(board, i, j, n, 'B'):
                return 'BLUE WINS'

    # If no winner, return NONE
    return 'NONE'


print(connect_n_win())
