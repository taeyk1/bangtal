from bangtal import*

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False) 

scene1 = Scene('퍼즐게임','images/원본.jpg')

startbutton = Object('images/start.png')
startbutton.locate(scene1, 580, 80)
startbutton.show()

scene2 = Scene('퍼즐게임','images/배경.png')

#왼쪽 166 위 462 사진크기 가로229 세로 123
puzzle1 = Object('images/1.jpg')
puzzle1.locate(scene2, 0, 565)
puzzle1.show()

puzzle2 = Object('images/2.jpg')
puzzle2.locate(scene2, 425, 565)
puzzle2.show()

puzzle3 = Object('images/3.jpg')
puzzle3.locate(scene2, 850, 565)
puzzle3.show()

puzzle4 = Object('images/4.jpg')
puzzle4.locate(scene2, 0, 285)
puzzle4.show()

puzzle5 = Object('images/5.jpg')
puzzle5.locate(scene2, 425, 285)
puzzle5.show()

puzzle6 = Object('images/6.jpg')
puzzle6.locate(scene2, 850, 285)
puzzle6.show()

puzzle7 = Object('images/7.jpg')
puzzle7.locate(scene2, 0, 0)
puzzle7.show()

puzzle8 = Object('images/8.jpg')
puzzle8.locate(scene2, 425, 0)
puzzle8.show()

puzzle9 = Object('images/9.jpg')
puzzle9.locate(scene2, 850, 0)
puzzle9.show()


def startbutton_onMouseAction(x, y, action):
    scene2.enter()
    showMessage('3x3퍼즐입니다. 맞추어 보세요!')
startbutton.onMouseAction =startbutton_onMouseAction
    
startGame(scene1)
