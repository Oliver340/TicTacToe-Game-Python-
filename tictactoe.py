theBoard = {'top-L' : ' ', 'top-M' : ' ','top-R' : ' ',
            'mid-L' : ' ', 'mid-M' : ' ','mid-R' : ' ',
            'low-L' : ' ', 'low-M' : ' ','low-R' : ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])




def win(board):
    if board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['mid-M'] == 'X' and board['top-M'] == 'X' and board['low-M'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X':
        print('X Wins')
        while True:
            input()
    if board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X':
        print('X Wins')
        while True:
            input()




    if board['top-L'] == '0' and board['top-M'] == '0' and board['top-R'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['top-L'] == '0' and board['mid-M'] == '0' and board['low-R'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['top-L'] == '0' and board['mid-L'] == '0' and board['low-L'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['mid-L'] == '0' and board['mid-M'] == '0' and board['mid-R'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['low-L'] == '0' and board['low-M'] == '0' and board['low-R'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['mid-M'] == '0' and board['top-M'] == '0' and board['low-M'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['top-R'] == '0' and board['mid-R'] == '0' and board['low-R'] == '0':
        print('0 Wins')
        while True:
            input()
    if board['top-R'] == '0' and board['mid-M'] == '0' and board['low-L'] == '0':
        print('0 Wins')
        while True:
            input()








turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    while True:
        while True:
            move = input()
            if move not in theBoard:
                continue
            break
        if theBoard[move] != ' ':
            continue
        else:
            break
        
    theBoard[move] = turn
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'
    win(theBoard)
printBoard(theBoard)
print('Tie')
while True:
    input()



    
