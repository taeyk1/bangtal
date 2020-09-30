from bangtal import*
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False) 

start = time.time()

scene1 = Scene('퍼즐게임','images/원본.jpg')

startbutton = Object('images/start.png')
startbutton.locate(scene1, 580, 80)
startbutton.show()

scene2 = Scene('퍼즐게임','images/배경.png')

def startbutton_onMouseAction(x, y, action):
    scene2.enter()
    showMessage('퍼즐을 풀어보세요!')
startbutton.onMouseAction =startbutton_onMouseAction

def find_index(object):
    for index in range(9):
        if game_board[index] == object: return index

def movable(index):
    if index < 0: return False
    if index > 8: return False
    if index % 3 > 0 and index - 1 == blank: return True  # 이동 : 왼쪽 오른쪽 아래 위
    if index % 3 < 2 and index + 1 == blank: return True
    if index > 2 and index - 3 == blank: return True
    if index < 6  and index + 3 == blank: return True
    return False

def move(index):
    global blank
    game_board[index].locate(scene2, 425 * (blank % 3), 560 - 280 * (blank // 3))
    game_board[blank].locate(scene2, 425 * (index % 3), 560 - 280 * (index // 3))

    game_board[index], game_board[blank] = game_board[blank], game_board[index]
    #object = game_board[index]
    #game_board[index] = game_board[blank]
    #game_board[blank] = object

    blank = index

def completed():
    for index in range(8):
        if game_board[index] != init_board[index]: return False
    return True
    
delta = [-1, 1, -3, 3]
def random_move():
    while True:
        index = blank + delta[random.randrange(4)]
        if movable(index): break
    move(index)
   

def onMouseAction_piece(object, x, y, action):
    index = find_index(object)
    if movable(index):
        move(index)

    if completed():
        print("걸린시간 :", time.time() - start)
        showMessage('성공!')

Object.onMouseActionDefault = onMouseAction_piece

game_board = []
init_board = []
for index in range(9): # 0~9 피스
    piece = Object("images/" +  str(index + 1) + ".jpg")
    piece.locate(scene2, 0 + 425 * (index % 3), 560 - 280 * (index // 3)) # 위치
    piece.show()
    
    game_board.append(piece)
    init_board.append(piece)


blank = 8
game_board[blank].hide()

count = 16
timer = Timer(1)
def onTimeout():
    random_move()

    global count
    count = count -1
    if count > 0:
        timer.set(0.1)
        timer.start()
timer.onTimeout = onTimeout

timer.start()

startGame(scene1)
