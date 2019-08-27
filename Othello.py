import random
import time
AIrandom = random.randint(0,3)
xcount = 0
ocount = 0
sqrs = 4
turn = 'X'
column = 0
row = 0
repeat1 = True
repeat2 = True
singleplayer = True
AIdirection = [  #This tells it which way to go (whether it goes from right to left or left to right, whether it goes up or down)
    (1,1, 0, 0),
    (1, -1, 0, 7),
    (-1, 1, 7, 0),
    (-1, -1, 7, 7),
]
a = [
    '        ',
    '        ',
    '        ',
    '   OX   ',
    '   XO   ',
    '        ',
    '        ',
    '        ',
]
def board(a):
    """
    This is prints out the board and shows where the Othello pieces are
    """
    print('    a   b   c   d   e   f   g   h')
    for index, row in enumerate(a):
        print('  ---------------------------------')
        print(index, end=' ')
        for character in row:
            print('|', character, end=' ')
        print('|')
    print('  ---------------------------------')
def place(row, column, turn):
    """
	This function (if that's what it's called) puts an X or an O in any place
	"""
    global a
    if 0<= column <= 7:
        newrow = ''
        for character in range (0, column):
            newrow += a[row][character]
        newrow += turn
        for character in range (column + 1,8):
            newrow += a[row][character]
        a[row] = newrow
def n(X): #This is used for switching turns
    if X == 'X':
        return 'O'
    elif X == 'O':
        return 'X'
print ('Do you want to \n [1]Play singleplayer \n [2]Play mulitplayer')
while repeat1 == True:
    pinput = input('Player input-->')
    if pinput == '1':
        repeat1 = False
    elif pinput == '2':
        singleplayer = False
        repeat1 = False
    else:
        print('Sorry, that\'s not a valid input')
board(a)
while sqrs != 64:
    possible = False
    if singleplayer == False or turn == 'X':
        print('Where do you want to place an ', turn, '?')
        pinput = input('Player input-->')
        if len(pinput) >= 2:
            if pinput[0] in('abcdefgh'): 
                if pinput[1] in('01234567'): #This bit turns the player input into a more usable format
                    column = ord(pinput[0])-ord('a')
                    row = int(pinput[1])
                else:
                    print('Sorry, that\'s not a valid place to put an', turn)
            elif pinput == 'Pass':
                print('Turn passed.')
                turn = n(turn)
            elif pinput == 'End':
                sqrs = 64
            else:
                print('Sorry, that\'s not a valid place on the board')
        else:
            print('Please phrase you input in the form of a coordinate (eg. a3), End, or Pass')
    elif singleplayer == True and turn == 'O': #I need to get the AI to pick the squares in a semi-unpredictable order
        if column in range (0,7):
            print(AIdirection[AIrandom][1])
            column += int(AIdirection[AIrandom][1])
        elif row in range (0,7):
            print(AIdirection[AIrandom][0])
            row += AIdirection[AIrandom][0]
            column = AIdirection[AIrandom][3]
        else:
            print ('AI: It looks like I don\'t have any possible moves')
            turn = n(turn)
    if a[row][column] == ' ':
        for x in range (-1,2):
            for y in range (-1, 2):
                try:
                    if a[row + y][column + x] == n(turn): #Trying to get it to determine whether somewhere is a valid place to put a X or O
                        z = 1
                        while a[row + (y*z)][column + (x*z)] == n(turn) and row + (y*z) in range (0,8) and column + (y*z) in range (0,8):
                            z = z + 1
                        if a[row + (y*z)][column + (x*z)] == turn:
                            place(row, column, turn)
                            possible = True
                            for w in range (1, (z + 1)):
                                place(row + (y*w), column + (x*w), turn)
                            if singleplayer == True:
                                AIrandom = random.randint(0,3)
                                if turn == 'O':
                                    time.sleep(5)
                except:
                    pass
        if possible == False:
            if singleplayer == False or turn == 'X':
                print('Sorry, that\'s not a valid place to put an', turn)
        elif possible == True:
            sqrs = sqrs + 1
            board(a)
            turn = n(turn)
            column = AIdirection[AIrandom][3]
            row = AIdirection[AIrandom][2]
    else:
        if singleplayer == False:
            print('Sorry, that space is already taken. Try again.')
for row in a: #This should only happen after everything else is finished
    for column in range(0,8):
        if row[column] == 'X':
            xcount += 1
        elif row[column] == 'O':
            ocount += 1
if xcount < ocount:
    print('Player O is the winner!')
elif xcount == ocount:
    print('It\'s a draw!')
else:
    print('Player X is the winner!')
