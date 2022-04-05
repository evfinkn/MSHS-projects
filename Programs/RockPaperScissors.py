import simplegui, random, time

mode = None
turn = 0
move = None
turn2 = 0
pastMove = None
aiMove = None
pastAiMove = None
huScore = 0
aiScore = 0
turn3 = 0
scoreUp = None
startTime = None
stop = False

def draw(canvas):
    global mode, turn, move, turn2, pastMove, aiMove, pastAiMove, huScore, aiScore, turn3, scoreUp, startTime, stop
    if (startTime != None):
        if (time.time() - startTime > 3):
            frame.stop()
    canvas.draw_line((300, 0), (300, 270), 2, 'white')
    canvas.draw_line((300, 330), (300, 600), 2, 'white')
    canvas.draw_text('Human', (106, 30), 30, 'white')
    canvas.draw_text('AI', (434.5, 30), 30, 'white')
    if (mode != None and turn != 0 and move != None):
        if (aiMove != None):
            pastAiMove = aiMove
        if (turn != turn2):
            aiMove = ai()
        if (move == "rock"):
            canvas.draw_text('Rock', (118.5, 300), 30, 'white')
        elif (move == "paper"):
            canvas.draw_text('Paper', (116, 300), 30, 'white')
        else:
            canvas.draw_text('Scissors', (101, 300), 30, 'white')
        if (aiMove == "rock"):
            canvas.draw_text('Rock', (418.5, 300), 30, 'white')
        elif (aiMove == "paper"):
            canvas.draw_text('Paper', (416, 300), 30, 'white')
        else:
            canvas.draw_text('Scissors', (401, 300), 30, 'white')
        if (turn != turn3):
            turn3 += 1
            if (move == "rock" and aiMove == "scissors" or move == "paper" and aiMove == "rock" or move == "scissors" and aiMove == "paper"):
                huScore += 1
                scoreUp = "player"
            elif (aiMove == "rock" and move == "scissors" or aiMove == "paper" and move == "rock" or aiMove == "scissors" and move == "paper"):
                aiScore += 1
                scoreUp = "ai"
            else:
                scoreUp = "tie"
        if (scoreUp == "player"):
            canvas.draw_text('beats', (269.5, 300), 30, 'white')
        elif (scoreUp == "ai"):
            canvas.draw_text('loses to', (255, 300), 30, 'white')
        elif (scoreUp == "tie"):
            canvas.draw_text('ties with', (249, 300), 30, 'white')
        if (mode == 1 and aiScore == 1 and stop != True):
            print ("The AI wins!")
            stop = True
            startTime = time.time()
        elif (mode == 1 and huScore == 1 and stop != True):
            print ("You win!")
            stop = True
            startTime = time.time()
        elif (mode == 3 and aiScore == 2 and stop != True):
            print ("The AI wins!")
            stop = True
            startTime = time.time()
        elif (mode == 3 and huScore == 2 and stop != True):
            print ("You win!")
            stop = True
            startTime = time.time()
        if (mode == 5 and aiScore == 3 and stop != True):
            print ("The AI wins!")
            stop = True
            startTime = time.time()
        elif (mode == 5 and huScore == 3 and stop != True):
            print ("You win!")
            stop = True
            startTime = time.time()
        
        
def ai():
    global pastMove, pastAiMove, turn2
    turn2 += 1
    if (pastMove != None):
        num = random.randint(0, 3)
        if (num == 0 or num == 1):
            #Other player plays what wasn't play last turn
            if (pastMove != "rock" and pastAiMove != "rock"):
                return "paper"
            elif (pastMove != "paper" and pastAiMove != "paper"):
                return "scissors"
            else:
                return "rock"
        elif (num == 2):
            #play what other person played
            return pastMove
        else:
            #Play random
            num = random.randint(0, 2)
            if (num == 0):
                return "rock"
            elif (num == 1):
                return "paper"
            else:
                return "scissors"
            
    else:
        num = random.randint(0, 2)
        if (num == 0):
            return "rock"
        elif (num == 1):
            return "paper"
        else:
            return "scissors"
    
def outOf1():
    global mode
    mode = 1
    label2 = frame.add_label('Pick your move:')
    button4 = frame.add_button('Rock', rock)
    button5 = frame.add_button('Paper', paper)
    button6 = frame.add_button('Scissors', scissors)
    
def outOf3():
    global mode
    mode = 3
    label2 = frame.add_label('Pick your move:')
    button4 = frame.add_button('Rock', rock)
    button5 = frame.add_button('Paper', paper)
    button6 = frame.add_button('Scissors', scissors)
    
def outOf5():
    global mode
    mode = 5
    label2 = frame.add_label('Pick your move:')
    button4 = frame.add_button('Rock', rock)
    button5 = frame.add_button('Paper', paper)
    button6 = frame.add_button('Scissors', scissors)
    
def rock():
    global move, turn, pastMove, stop
    if (move != None):
        pastMove = move
    if (stop != True):
        move = "rock"
        turn += 1
    
def paper():
    global move, turn, pastMove, stop
    if (move != None):
        pastMove = move
    if (stop != True):
        move = "paper"
        turn += 1
    
def scissors():
    global move, turn, pastMove, stop
    if (move != None):
        pastMove = move
    if (stop != True):
        move = "scissors"
        turn += 1
    
    
frame = simplegui.create_frame('Rock Paper Scissors', 600, 600)
label1 = frame.add_label('Out of:')
button1 = frame.add_button('1', outOf1)
button2 = frame.add_button('3', outOf3)
button3 = frame.add_button('5', outOf5)
frame.set_draw_handler(draw)
frame.start()