def Valid_Sudoku(inp):
    rows = {}
    cols = {}
    boxes = {}

    for i in range(9):
        for j in range(9):
            num = inp[i][j]
            if num != '.':
                box_index = (i // 3) * 3 + (j // 3)

                if (i, num) in rows or (j, num) in cols or (box_index, num) in boxes:
                    return False

                rows[(i, num)] = True
                cols[(j, num)] = True
                boxes[(box_index, num)] = True

    return True

#_____Main______

input1=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
if __name__ == "__main__":
    print(Valid_Sudoku(input1))
