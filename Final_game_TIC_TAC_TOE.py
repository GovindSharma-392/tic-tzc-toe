def p_board(board):
    s = '''
    0|1|2       {} | {} | {}
    -+-+-       --+---+--
    3|4|5       {} | {} | {}
    -+-+-       --+---+--
    6|7|8       {} | {} | {}
    '''. format(*board)
    print(s)



# main code 
count=1
while 1 :
    print('\n\nWelocome to the Tic Toe Game ')
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    turn = 'X'
    for i in range(0,10):

        p_board(board)
        print(f'Its your turn {turn}. move to which place ?')
        choice = int(input())
        count+=1
        

        if board[choice] == ' ':
            board[choice] = turn
        else:
            print('Place Already Filled Move to next place ')
            count-1
            continue


        if board[0] == board[1] == board[2] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[0] == board[3] == board[6] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[6] == board[7] == board[8] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[3] == board[4] == board[5] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[1] == board[4] == board[7] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[0] == board[4] == board[8] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[2] == board[5] == board[8] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif board[2]== board[4] == board[6] != ' ':
            p_board(board)
            print('--------GAME OVER---------')
            print(f'*****{turn} WON *****\n')
            break
        elif count==10:
            print('No One WON \n Try Again\n\n')
            break

        # change the player after every move 
        turn = 'X' if turn != 'X' else 'O'