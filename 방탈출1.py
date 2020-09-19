from bangtal import *
# pip install bangtal

scene1 = Scene('룸1','images/배경-1.png')


door1 = Object('images/문-오른쪽-닫힘.png')
door1.locate(scene1, 800, 270)
door1.show()
door1.closed= True

key = Object('images/열쇠.png')
key.setScale(0.2)
key.locate(scene1, 600, 150)
key.show()

flowerpot = Object('images/화분.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

scene2 = Scene('룸2','images/배경-2.png')

door2 = Object('images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()
door2.closed= True

door3 = Object('images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.show()
door3.closed= True

keypad = Object('images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad .show()

switch = Object('images/스위치.png')
switch.locate(scene2, 880, 440)
switch .show()

password = Object('images/탈출.png')
password.locate(scene2,500, 100)

keycard = Object('images/키카드.png')
keycard.locate(scene2, 500, 500)
keycard.setScale(0.4)
keycard.show()

picture = Object('images/액자.jpg')
picture.locate(scene2, 430, 500)
picture.setScale(0.9)
picture.show()


scene3 = Scene('룸3','images/배경-1.png')

door4 = Object('images/문-왼쪽-열림.png')
door4.locate(scene3, 140, 269)
door4.show()
door4.closed= True

door5 = Object('images/문-오른쪽-닫힘.png')
door5.locate(scene3, 800, 270)
door5.show()
door5.closed= True

d = Object('images/드라이버.png')
d.setScale(0.2)
d.locate(scene3, 600, 150)
d.show()


#문이 닫혀있으면
#   키를 가지고 있으면
#       문을 열어준다
#       그렇지 않으면 문자를 보여준다
#   그렇지 않으면 게임을 종료한다.

def door1_onMouseAction(x, y, action):
    if door1.closed:
        if key.inHand():
            door1.setImage('images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요합니다.')
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()
    showMessage('열쇠를 얻었다.')
key.onMouseAction = key_onMouseAction

flowerpot.moved = False
def flowerpot_onMouseAction(x, y, action):
    if flowerpot.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot.locate(scene1, 450, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot.locate(scene1, 650, 150)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_UP:
            flowerpot.locate(scene1, 450, 250)
            flowerpot.moved = True
        elif action == MouseAction.DRAG_DOWN:
            flowerpot.locate(scene1, 650, 50)
            flowerpot.moved = True

flowerpot.onMouseAction = flowerpot_onMouseAction

def door2_onMouseAction(x, y, action):
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

door3.locked= True
def door3_onMouseAction(x, y, action):
    if door3.locked:
        showMessage('바닥에 뭐라고 적혀 있는 것 같은데?')
    elif door3.closed:
        door3.setImage('images/문-오른쪽-열림.png')
        door3.closed = False
    else:
        scene3.enter()
door3.onMouseAction = door3_onMouseAction

def door3_onKeypad():
    door3.locked = False
    showMessage('문이 열렸다!!!')
door3.onKeypad = door3_onKeypad

def keypad_onMouseAction(x, y, action):
    showKeypad('ESCAPE', door3)
keypad.onMouseAction = keypad_onMouseAction

switch.lighted = True
def switch_onMouseAction(x, y, action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password .hide() 
    else:
        scene2.setLight(0.25)
        password .show()
switch.onMouseAction = switch_onMouseAction

def picture_onMouseAction(x, y, action):
     if d.inHand():
            picture.hide()
     else:
         showMessage('액자뒤에 뭐가 있는데?')
picture.onMouseAction = picture_onMouseAction

def keycard_onMouseAction(x, y, action):
    keycard.pick()
    showMessage('키카드를 얻었다.')
keycard.onMouseAction = keycard_onMouseAction

def door4_onMouseAction(x, y, action):
    scene2.enter()
door4.onMouseAction = door4_onMouseAction

def d_onMouseAction(x, y, action):
    d.pick()
d.onMouseAction = d_onMouseAction

door5.closed = True
def door5_onMouseAction(x, y, action):
    if door5.closed:
        if keycard.inHand():
            door5.setImage('images/문-오른쪽-열림.png')
            door5.closed = False
            showMessage('수고하셨습니다.')
        else:
            showMessage('키카드가 필요합니다')
    else:
        endGame()
door5.onMouseAction = door5_onMouseAction

startGame(scene1)
