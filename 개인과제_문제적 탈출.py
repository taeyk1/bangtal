from bangtal import*
import time

scene1 = Scene('문제적 탈출','images/게임화면.png')

start = time.time()

startbutton = Object('images/start.png')
startbutton.locate(scene1, 600, 80)
startbutton.show()

title1 = Object('images/문제적.png')
title1.locate(scene1, 760, 370)
title1.show()

title2 = Object('images/탈출.png')
title2.locate(scene1, 850, 270)
title2.show()

scene2 = Scene('문제적 탈출','images/방1.png')

door1 = Object('images/문.png')
door1.locate(scene2, 350, 200)
door1.setScale(0.4)
door1.show()

keypad1 = Object('images/키패드.png')
keypad1.locate(scene2, 500, 420)
keypad1 .show()

problem1 = Object('images/문제1.png')
problem1.locate(scene2, 700, 420)
problem1.show()

text = Object('images/메모.jpg')
text.locate(scene2, 600, 120)
text.setScale(0.4)
text .show()

scene3 = Scene('문제적 탈출','images/방2.png')

door2 = Object('images/문.png')
door2.locate(scene3, 350, 200)
door2.setScale(0.4)
door2.show()

problem2 = Object('images/문제2.png')
problem2.locate(scene3, 650, 420)
problem2.setScale(0.4)
problem2 .show()

keypad2 = Object('images/키패드.png')
keypad2.locate(scene3, 500, 420)
keypad2 .show()

scene4 = Scene('문제적 탈출','images/방3.png')

door3 = Object('images/문.png')
door3.locate(scene4, 700, 180)
door3.setScale(0.4)
door3.show()

problem3 = Object('images/문제3.png')
problem3.locate(scene4, 330, 420)
problem3.setScale(0.4)
problem3 .show()

key = Object('images/열쇠.png')
key.setScale(0.4)
key.locate(scene4, 500, 150)

box = Object('images/금고.png')
box.setScale(0.1)
box.locate(scene4, 450, 150)
box.show()

keypad3 = Object('images/키패드.png')
keypad3.locate(scene4, 530, 230)
keypad3.show()

scene5 = Scene('문제적 탈출','images/방4.png')

door4 = Object('images/문.png')
door4.locate(scene5, 550, 100)
door4.setScale(0.4)
door4.show()

keypad4 = Object('images/키패드.png')
keypad4.locate(scene5, 700, 350)
keypad4 .show()

hint = Object('images/힌트.jpg')
hint.locate(scene5, 300, 70)
hint.setScale(0.4)
hint .show()

problem4 = Object('images/문제4.png')
problem4.locate(scene5, 100, 450)
problem4.setScale(0.6)
problem4 .show()

heart = Object('images/하트.png')
heart.locate(scene5, 570, 450)
heart.setScale(0.1)
heart .show()

problem5 = Object('images/문제5.png')
problem5.locate(scene5 , 770, 450)
problem5.setScale(0.6)
problem5 .show()

def startbutton_onMouseAction(x, y, action):
    scene2.enter()
    showMessage('문제로 가득찬 방을 탈출하시오.')
startbutton.onMouseAction =startbutton_onMouseAction

door1.locked = True
def door1_onMouseAction(x, y, action):
    if door1.locked:
        showMessage('문이 잠겼습니다.')
    else:
        scene3.enter()
door1.onMouseAction = door1_onMouseAction

def text_onMouseAction(x, y, action):
    showMessage('제작자의 성의를 생각하여 답을 찍지말아주세요ㅠㅠ')
text.onMouseAction = text_onMouseAction

def door1_onKeypad():
    door1.locked = False
    showMessage('♥는 %였어!')
door1.onKeypad = door1_onKeypad

def keypad1_onMouseAction(x, y, action):
    showKeypad('2', door1)
keypad1.onMouseAction = keypad1_onMouseAction

def problem1_onMouseAction(x, y, action):
    showMessage('♥가 무슨 연산자를 의미하는 거 같은걸?')
problem1.onMouseAction = problem1_onMouseAction


door2.locked = True
def door2_onMouseAction(x, y, action):
    if door2.locked:
        showMessage('문이 잠겼습니다.')
    else:
        scene4.enter()
        showMessage('지금까지 몸풀기였어...')
door2.onMouseAction = door2_onMouseAction

def keypad2_onMouseAction(x, y, action):
    showKeypad('I', door2)
keypad2.onMouseAction = keypad2_onMouseAction

def door2_onKeypad():
    door2.locked = False
    showMessage('one two three four five six의 두번째 글자였어!')
door2.onKeypad = door2_onKeypad

def problem2_onMouseAction(x, y, action):
    showMessage('12345')
problem2.onMouseAction = problem2_onMouseAction

door3.closed= True
def door3_onMouseAction(x, y, action):
    if door3.closed:
            if key.inHand():
                showMessage('문이 열렸어!')
                door3.closed = False
            else:
                showMessage('열쇠가 필요해.')
    else:
        scene5.enter()
        showMessage('마지막인 것 같군')
door3.onMouseAction = door3_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()
key.onMouseAction = key_onMouseAction

box.locked = True
def box_onMouseAction(x, y, action):
    if box.locked:
        showMessage('금고안에 뭐가 들어있어...')
box.onMouseAction = box_onMouseAction

def keypad3_onMouseAction(x, y, action):
    showKeypad('TEN', box)
keypad3.onMouseAction = keypad3_onMouseAction

def box_onKeypad():
    box.locked = False
    box.hide()
    keypad3.hide()
    key.show()
    showMessage('田 - 口= 十 이구나!!!')
box.onKeypad = box_onKeypad

def problem3_onMouseAction(x, y, action):
    showMessage('한자와 관련된 것 같아')
problem3.onMouseAction = problem3_onMouseAction

door4.locked = True
def door4_onMouseAction(x, y, action):
    if door4.locked:
        showMessage('문이 잠겼습니다.')
    else:
        print("걸린시간 :", time.time() - start)
        endGame()
door4.onMouseAction = door4_onMouseAction

def keypad4_onMouseAction(x, y, action):
    showKeypad('THREE', door4)
keypad4.onMouseAction = keypad4_onMouseAction

def door4_onKeypad():
    door4.locked = False
    showMessage('수고하셨습니다! 걸린시간을 확인하세요.')
door4.onKeypad = door4_onKeypad

def hint_onMouseAction(x, y, action):
    showMessage('1.숫자 뒤집기 2.하트 3.획')
hint.onMouseAction = hint_onMouseAction

def problem4_onMouseAction(x, y, action):
    showMessage('이 숫자들... 무엇을 의미 하는 걸까?')
problem4.onMouseAction = problem4_onMouseAction

def problem5_onMouseAction(x, y, action):
    showMessage('복잡하군...')
problem5.onMouseAction = problem5_onMouseAction

startGame(scene5)
