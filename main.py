def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def clear_output():
    print('\n' * 100)


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1 , choose X or O: ')

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
 pass

if __name__ == '__main__':
    test_board = ['X', "o", 'X', "o", 'X', "o", 'X', "o", 'X', "o", ]
    place_marker(test_board, '$', 8)
    display_board(test_board)
