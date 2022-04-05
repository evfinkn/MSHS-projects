import simplegui, random, time
huPlayer1 = 1
huPlayer2 = 2
aiPlayer = 3
player = None
count = 0
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
boolean = False
stop = False
startTime = None

def mouse_handler(position):
    global player, huPlayer1, huPlayer2, board
    #Make sure it's player's turn
    if (not stop and player == huPlayer1 or not stop and player == huPlayer2 and aiPlayer == 3):
        #Puts the symbol on the location of click
        for x in range(0, 600):
            for y in range(0, 600):
                if (position == (x, y)):
                    #Left Column
                    if (x < 200):
                        #Top Row
                        if (y < 200):
                            #Make sure spot isn't taken
                            if (board[0] == 0):
                                board[0] = player
                                changeTurn()
                        #Middle Row
                        elif (y > 200 and y < 400):
                            if (board[3] == 3):
                                board[3] = player
                                changeTurn()
                        #Bottom Row
                        elif (y > 400):
                            if (board[6] == 6):
                                board[6] = player
                                changeTurn()
                    #Middle Column
                    elif (x > 200 and x < 400):
                        #Top Row
                        if (y < 200):
                            if (board[1] == 1):
                                board[1] = player
                                changeTurn()
                        #Middle Row
                        elif (y > 200 and y < 400):
                            if (board[4] == 4):
                                board[4] = player
                                changeTurn()
                        #Bottom Row
                        elif (y > 400):
                            if (board[7] == 7):
                                board[7] = player
                                changeTurn()
                    #Right Column
                    elif (x > 400):
                        #Top Row
                        if (y < 200):
                            if (board[2] == 2):
                                board[2] = player
                                changeTurn()
                        #Middle Row
                        elif (y > 200 and y < 400):
                            if (board[5] == 5):
                                board[5] = player
                                changeTurn()
                        #Bottom Row
                        elif (y > 400):
                            if (board[8] == 8):
                                board[8] = player
                                changeTurn()
                                
def changeTurn():
    global player, aiPlayer, huPlayer1, huPlayer2
    #No AI
    if (aiPlayer == 3):
        if (player == huPlayer1):
            player = huPlayer2
        else:
            player = huPlayer1
    #AI
    else:
        if (player == huPlayer1):
            player = aiPlayer
        else:
            player = huPlayer1
                    
def draw(canvas):
    global stop, startTime, player, aiPlayer, huPlayer1, huPlayer2, board, count, boolean
    #Stops frame after 3 seconds have passed after a win
    if (startTime != None):
        if (time.time() - startTime > 3):
            frame.stop()
    #Checks for Player 1 win
    if (winning(board, huPlayer1) and stop != True):
        print ("Player " + huPlayer1 + " wins!")
        stop = True
        startTime = time.time()
    #Checks for Player 2 win
    elif (winning(board, huPlayer2) and stop != True):
        print ("Player " + huPlayer2 + " wins!")
        stop = True
        startTime = time.time()
    #Checks for a draw
    if (not winning(board, huPlayer2) and not winning(board, huPlayer1) and not winning(board, aiPlayer) and board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8):
        print ("It's a draw.")
        frame.stop()
    #AI's move
    if (player == aiPlayer and huPlayer2 == 2 and not winning(board, aiPlayer)):
        bestSpot = minimax(board, player)
        count = 0
        board[bestSpot[0]] = player
        if (winning(board, player)):
            print ("The AI wins!")
            stop = True
            startTime = time.time()
        else:
            changeTurn()
    #Lines forming nine spots
    canvas.draw_line((200, 0), (200, 600), 5, 'white')
    canvas.draw_line((400, 0), (400, 600), 5, 'white')
    canvas.draw_line((0, 200), (600, 200), 5, 'white')
    canvas.draw_line((0, 400), (600, 400), 5, 'white')
    #Top left
    if (not board[0] == 0):
        if (board[0] == "x"):
            canvas.draw_line((10, 10), (190, 190), 5, 'white')
            canvas.draw_line((190, 10), (10, 190), 5, 'white')
        elif (board[0] == "o"):
            canvas.draw_circle((100, 100), 90, 5, 'white')
    #Top Middle
    if (not board[1] == 1):
        if (board[1] == "x"):
            canvas.draw_line((210, 10), (390, 190), 5, 'white')
            canvas.draw_line((390, 10), (210, 190), 5, 'white')
        elif (board[1] == "o"):
            canvas.draw_circle((300, 100), 90, 5, 'white')
    #Top Right
    if (not board[2] == 2):
        if (board[2] == "x"):
            canvas.draw_line((410, 10), (590, 190), 5, 'white')
            canvas.draw_line((590, 10), (410, 190), 5, 'white')
        elif (board[2] == "o"):
            canvas.draw_circle((500, 100), 90, 5, 'white')
    #Middle Left
    if (not board[3] == 3):
        if (board[3] == "x"):
            canvas.draw_line((10, 210), (190, 390), 5, 'white')
            canvas.draw_line((190, 210), (10, 390), 5, 'white')
        elif (board[3] == "o"):
            canvas.draw_circle((100, 300), 90, 5, 'white')
    #Center
    if (not board[4] == 4):
        if (board[4] == "x"):
            canvas.draw_line((210, 210), (390, 390), 5, 'white')
            canvas.draw_line((390, 210), (210, 390), 5, 'white')
        elif (board[4] == "o"):
            canvas.draw_circle((300, 300), 90, 5, 'white')
    #Middle Right
    if (not board[5] == 5):
        if (board[5] == "x"):
            canvas.draw_line((410, 210), (590, 390), 5, 'white')
            canvas.draw_line((590, 210), (410, 390), 5, 'white')
        elif (board[5] == "o"):
            canvas.draw_circle((500, 300), 90, 5, 'white')
    #Bottom Left
    if (not board[6] == 6):
        if (board[6] == "x"):
            canvas.draw_line((10, 410), (190, 590), 5, 'white')
            canvas.draw_line((190, 410), (10, 590), 5, 'white')
        elif (board[6] == "o"):
            canvas.draw_circle((100, 500), 90, 5, 'white')
    #Bottom Middle
    if (not board[7] == 7):
        if (board[7] == "x"):
            canvas.draw_line((210, 410), (390, 590), 5, 'white')
            canvas.draw_line((390, 410), (210, 590), 5, 'white')
        elif (board[7] == "o"):
            canvas.draw_circle((300, 500), 90, 5, 'white')
    #Bottom Right
    if (not board[8] == 8):
        if (board[8] == "x"):
            canvas.draw_line((410, 410), (590, 590), 5, 'white')
            canvas.draw_line((590, 410), (410, 590), 5, 'white')
        elif (board[8] == "o"):
            canvas.draw_circle((500, 500), 90, 5, 'white')   
        
def minimax(board, player):
    global huPlayer1, aiPlayer, count
    availSpots = emptyIndexies(board)
    
    count += 1
    if (count >= 1000):
        return 0
    
    if (winning(board, huPlayer1)):
        return -10
    elif (winning(board, aiPlayer)):
        return 10
    elif (len(availSpots) == 0):
        return 0
    
    moves = []
    for x in range(len(availSpots)):
        move = []
        move.append(board[availSpots[x]])
        
        board[availSpots[x]] = player
        
        if (player == aiPlayer):
            result = minimax(board, huPlayer1)
            if (type(result) == type([1, 2])):
                move.append(result[1])
            else:
                move.append(result)
        else:
            result = minimax(board, aiPlayer)
            move.append(result)
            
        board[availSpots[x]] = move[0]
        
        moves.append(move)
        
    bestMove = None
    if (player == aiPlayer):
        bestScore = -10000
        for x in range(len(moves)):
            if (moves[x][1] > bestScore):
                bestScore = moves[x][1]
                bestMove = x
    else:
        bestScore = 10000
        for x in range(len(moves)):
            if (moves[x][1] < bestScore):
                bestScore = moves[x][1]
                bestMove = x
    if (bestMove == None):
        bestMove = random.randint(0, len(moves) - 1)
    return moves[bestMove]
    
def emptyIndexies(board):
    indexies = []
    for spot in board:
        if (spot != "x" and spot != "o"):
            indexies.append(spot)
    return indexies

def winning(board, player):
    if (board[0] == player and board[1] == player and board[2] == player or 
        board[3] == player and board[4] == player and board[5] == player or 
        board[6] == player and board[7] == player and board[8] == player or 
        board[0] == player and board[3] == player and board[6] == player or 
        board[1] == player and board[4] == player and board[7] == player or 
        board[2] == player and board[5] == player and board[8] == player or 
        board[0] == player and board[4] == player and board[8] == player or 
        board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False
        
def playFriend():
    global huPlayer1, huPlayer2, player
    if (aiPlayer == 3 and huPlayer2 == 2):
        huPlayer1 = "x"
        huPlayer2 = "o"
        player = huPlayer1
        label3 = frame.add_label('Player X goes first.')
    
def playAI():
    global aiPlayer
    if (huPlayer2 == 2 and aiPlayer == 3):
        aiPlayer = True
        label2 = frame.add_label('Do you want to be X or O?')
        button3 = frame.add_button('X', xSymbol)
        button4 = frame.add_button('O', oSymbol)
    
def xSymbol():
    global huPlayer1, aiPlayer, player
    if (aiPlayer == True):
        huPlayer1 = "x"
        aiPlayer = "o"
        if (random.randint(0, 1) == 0):
            label3 = frame.add_label('The AI goes first.')
            player = aiPlayer
        else:
            label3 = frame.add_label('You go first.')
            player = huPlayer1
        
def oSymbol():
    global huPlayer1, aiPlayer, player
    if (aiPlayer == True):
        huPlayer1 = "o"
        aiPlayer = "x"
        if (random.randint(0, 1) == 0):
            label3 = frame.add_label('The AI goes first.')
            player = aiPlayer
        else:
            label3 = frame.add_label('You go first.')
            player = huPlayer1
    
frame = simplegui.create_frame('Tic Tac Toe', 600, 600)
frame.set_mouseclick_handler(mouse_handler)
label1 = frame.add_label('Who are you playing with?')
button1 = frame.add_button('Friend', playFriend)
button2 = frame.add_button('AI', playAI)
frame.set_draw_handler(draw)
frame.start()