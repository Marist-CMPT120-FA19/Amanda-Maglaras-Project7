#Amanda Maglaras
#amanda.maglaras1marist.edu
#This project allows us to score an archery game played by the user



from graphics import *
import math


#distance
def distance(point, circle):
    x = point.getX() - circle.getCenter().getX()
    y = point.getY() - circle.getCenter().getY()
    dist = math.sqrt(x*x + y*y)

    return dist <= circle.getRadius()

    
def main():

    score=0
    
    win = GraphWin('Archery Scorer',280,280)
    center=Point(150, 150)
#make the colored circles
    white=Circle(center,100)
    white.setFill("white")
    white.draw(win)

    purple=Circle(center,80)
    purple.setFill("purple")
    purple.draw(win)

    green=Circle(center, 60)
    green.setFill("green")
    green.draw(win)

    blue=Circle(center, 40)
    blue.setFill("blue")
    blue.draw(win)

    yellow=Circle(center,20)
    yellow.setFill("yellow")
    yellow.draw(win)
#assign each circle point values
    for x in range(5):
        click= win.getMouse()
        cir = Circle(click, 5)
        cir.draw(win)
        cir.setFill("pink")
        if(distance(click, yellow)):
            score += 9
            print("+9")
        elif(distance(click, blue)):
            score += 7
            print("+7")
        elif(distance(click, green)):
            score += 5
            print("+5")
        elif(distance(click, purple)):
            score += 3
            print("+3")
        elif(distance(click, white)):
            score += 1
            print("+1")
        else:
            score += 0
            print("+0")
    
    
    print("Total Points: ", score)
#click to close window
    end= Text(Point(win.getWidth()/2,20), "Click to Quit")
    end.draw(win)

                    
    win.getMouse()
    win.close()
    
main()
