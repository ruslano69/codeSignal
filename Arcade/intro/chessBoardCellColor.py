def chessBoardCellColor(cell1, cell2):
    board = {"A":1, "B":2, "C":3, "D":4,"E":5,"F":6, "G":7, "H":8}
    total01 = board[cell1[0]] + int(cell1[1])
    total02 = board[cell2[0]] + int(cell2[1])
    
    return total01 % 2 == total02 % 2