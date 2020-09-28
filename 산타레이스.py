from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)
scene = Scene('산타레이스','산타이미지/background.png') 

santa = Object('산타이미지/santa.png')
santa.x = 0
santa.y = 500
santa.locate(scene, santa.x, santa.y)
santa.show()

playButton = Object('산타이미지/play.png')
playButton.locate(scene, 610, 30)

startButton = Object('산타이미지/start.png')
startButton.locate(scene, 590, 70)
startButton.show()

endButton = Object('산타이미지/end.png')
endButton.locate(scene, 590, 20)
endButton.show()

timer = Timer(10.)
showTimer(timer)

def playButton_onMouseAction(x, y, action):
    santa.x = santa.x + 30
    santa.locate(scene, santa.x, santa.y)

    if santa.x > 1280:
        showMessage('선물배달성공~~!!!')
        
        startButton.setImage('산타이미지/restart.png')
        startButton.show()
        endButton.show()
        playButton.hide()

        timer.stop()

playButton.onMouseAction = playButton_onMouseAction

def startButton_onMouseAction(x, y, action):
    startButton.hide()
    endButton.hide()
    playButton.show()

    timer.set(10.)
    timer.start()

    santa.x = 0
    santa.locate(scene, santa.x, santa.y)
startButton.onMouseAction = startButton_onMouseAction

def endButton_onMouseAction(x, y, action):
    endGame()
endButton.onMouseAction = endButton_onMouseAction

def timer_onTimeout():
    showMessage('선물 배달 실패')

    startButton.setImage('산타이미지/restart.png')
    startButton.show()
    endButton.show()
    playButton.hide()
timer.onTimeout = timer_onTimeout

startGame(scene)
