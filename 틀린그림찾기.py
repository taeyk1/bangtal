from bangtal import*

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False) 

scene = Scene('틀린그림찾기','images/problem.png')

problem = Object('images/problem.png')
problem.locate(scene, 0, 0)
problem.show()

class Rect:
    def __init__(self, cx, cy ,r):
        self.centerX = cx
        self.centerY = cy
        self.radius = r

    def checkin(self, x, y):
        return self.centerX - self.radius < x < self.centerX + self.radius and self.centerY - self.radius < y < self.centerY + self.radius

check_margin = 25
class DifferencePoint:
    def __init__(self, lcx, rcx, cy, r):
        self.left_rect = Rect(lcx, cy, r)
        self.right_rect = Rect(rcx, cy, r)
        self.left_check = Object('Images/check.png')
        self.left_check.locate(scene, lcx - check_margin , cy - check_margin)
        self.right_check = Object('Images/check.png')
        self.right_check.locate(scene, rcx - check_margin , cy - check_margin)
        self.found =False
    def checkin(self, x, y):
        return self.left_rect.checkin(x, y) or self.right_rect.checkin(x, y)

    def show(self):
        self.left_check.show()
        self.right_check.show()
        self.found =True

#달 좌우 (568,594) = 54  (1186,594) = 54
points = [
    DifferencePoint(568, 1186, 594, 54),
    DifferencePoint(99, 717, 551, 17),
    DifferencePoint(383, 1001, 482, 16),
    DifferencePoint(401, 1019, 158, 27),
    DifferencePoint(61, 679, 255, 36),
    DifferencePoint(592, 1210, 421, 35),
    DifferencePoint(320, 938, 117, 13),
    ]

count = 0
def problem_onMouseAction(x, y, action):
    wrong = True
    for p in points:
        if p.checkin(x, y):
             wrong = False
             if p.found == False:
                global count
                p.show() 
                count+=1
           


    if count == 7:
        showMessage('성공 7개 다 찾았다')

    if wrong:
        endGame()

problem.onMouseAction = problem_onMouseAction

showMessage('틀린 곳을 찾아보세요.')
startGame(scene)