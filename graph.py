from graphics import *
from random import *
import time

winTitle = "Lines and Circles"
winSizeW = 800
winSizeH = 600
radius = 5
coords = list()
circlesCount = 0
linesCount = 0

win = GraphWin(winTitle, winSizeW, winSizeH)

randomPointsCount = randint(4, 30)

for i in range(0, randomPointsCount):
    randX = randint(25, 775)
    randY = randint(25, 575)

    pt = Point(randX, randY)
    coords.append(pt)

    cir = Circle(pt, radius)
    circlesCount += 1
    cir.draw(win)
    
print(circlesCount)
"""
for i in range(0, randomPointsCount - 1):
    line = Line(coords[i], coords[i + 1])
    line.draw(win)
    time.sleep(0.15)
"""
for i in range(0, randomPointsCount - 1):
    # print('i is', i)
    linesCount += 1
    for j in range(0, randomPointsCount):
        # print('j is', j)
        linesCount += 1
        line = Line(coords[i], coords[j])
        line.draw(win)
    time.sleep(0.1)
    
print(linesCount)

win.getKey()
win.close()