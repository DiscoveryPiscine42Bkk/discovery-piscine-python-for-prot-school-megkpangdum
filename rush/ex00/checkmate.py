def checkmate(board):  
    def find_king(board):   #find_king
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == 'K':
                    return i, j
        return None


    def can_capture_king(board, king_pos, piece, directions):  #checkpiece
        kx, ky = king_pos
        for direction in directions:
            x, y = kx, ky
            while True:
                x += direction[0]
                y += direction[1]
                if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                    break
                if board[x][y] == 'K' and piece != 'K':  
                    return True
                if board[x][y] != '.':  
                    break
        return False


    def pawn_can_capture_king(board, king_pos, pawn_pos): #checkpawn
        kx, ky = king_pos
        px, py = pawn_pos
        pawn_moves = [(-1, -1), (-1, 1)] 
        for move in pawn_moves:
            if (kx == px + move[0] and ky == py + move[1]):
                return True
        return False


    board = [list(row) for row in board.splitlines()]  #checkkinginbord
    king_pos = find_king(board)

    if not king_pos:
        print("Error: No King found.")
        return

  #piece
    directions_rook = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    directions_bishop = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    directions_pawn = [(-1, -1), (-1, 1)]
    directions_queen = directions_rook + directions_bishop + directions_pawn

    for i, row in enumerate(board):  #loopcheckking
        for j, cell in enumerate(row):


            if cell == 'Q' and can_capture_king(board, king_pos, cell, directions_queen):
                print("Success: King can be captured by Queen")
                return
            if cell == 'R' and can_capture_king(board, king_pos, cell, directions_rook):
                print("Success: King can be captured by Rook")
                return
            if cell == 'B' and can_capture_king(board, king_pos, cell, directions_bishop):
                print("Success: King can be captured by Bishop")
                return
            if cell == 'P' and pawn_can_capture_king(board, king_pos, (i, j)):
                print("Success: King can be captured by Pawn")
                return


    print("Fail: King cannot be captured.")