def main():  
    # reading from input file
    with open('input.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]

    draw, all_boards = load_input(lines)

    total, drawn_numbers = 0, []
    print(draw)
    print("PART I")
    for number in draw:
        drawn_numbers.append(number)       
        is_winner, board = check_boards(all_boards, drawn_numbers)
        if is_winner:
            print(f"Last Drawn Number: {number}")
            print("Drawn Numbers:")
            print(drawn_numbers)
            print("Board: ")
            print(board)
            
            # getting sum
            for row in board:
                for col in row:
                    if col not in drawn_numbers:
                        total += int(col)            
            break
    print(total * int(number))
    
        
    print("PART II")
    # Keep reusing check_boards and removing winning board from all boards
    # Until there is only one board left.
    #drawn_numbers = []
    last_board_removed = []
    while len(all_boards) > 0:
        drawn_numbers = []
        for number in draw:
            drawn_numbers.append(number)       
            is_winner, board = check_boards(all_boards, drawn_numbers)  
            if is_winner:
                all_boards.remove(board)
                last_board_removed = board
                break

    print("The board that wins last is: ")
    print(last_board_removed)
    print(drawn_numbers)
    print(drawn_numbers[-1])
    # getting sum
    total = 0
    for row in last_board_removed:
        for col in row:
            if col not in drawn_numbers:
                total += int(col) 
    print(total)  #25026 - too high
    print(total * int(drawn_numbers[-1]))    


def horizontal_check(board, drawn_numbers):   
    for row in board:    
        is_winner = True
        for i in range(0, 5):
            if row[i] not in drawn_numbers:
                is_winner = False
                break
        if is_winner:
            break
    return is_winner

def vertical_check(board, drawn_numbers):
    for i in range(0, 5):
        is_winner = True
        for row in board:
            if row[i] not in drawn_numbers:
                is_winner = False
                break
        if is_winner:
            break

    return is_winner  

def diagonal_check(board, drawn_numbers):
    is_winner = True
    
    # diagonal top-left to bottom-right
    for x in range(0, 5):
        if board[x][x] not in drawn_numbers:
            is_winner = False
    
    # probably separate into two functions
    if is_winner:
        return is_winner
    
    # diagonal top-right to bottom-left   
    is_winner = True
    for x in range(0, 5):
        y = 4 - x
        if board[x][y] not in drawn_numbers:
            is_winner = False
    
    return is_winner

def check_boards(all_boards, drawn_numbers):
    # implement functions to search
    # horizontally, vertically, and diagonally
    for board in all_boards:
        #horizontal_check(board, drawn_numbers)
        #vertical_check(board, drawn_numbers)
        if horizontal_check(board, drawn_numbers) or vertical_check(board, drawn_numbers):
        #or diagonal_check(board, drawn_numbers):    
            return True, board

    return False, []
    
def load_input(lines):
    draw = lines[0].split(',')
    b = ""
    
    for i in range(2, len(lines)):
        b += lines[i] + ' '
    b = b.replace('   ', ' ').replace('  ',' ').strip().split(' ')

    board = []
    all_boards = []
    for i in range(0, len(b) + 5, 5):
        if i % 25 == 0 and i != 0:
            all_boards.append(board)
            board = []

        board.append(b[i:i+5])

    return draw, all_boards

  
if __name__ == "__main__":
    main()