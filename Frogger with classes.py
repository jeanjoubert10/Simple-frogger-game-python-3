# Frogger with classes
# Jean Joubert 6 November 2019
# Created with IDLE on mac osx
# audio os system afplay (winsound for windows)
# Some settings may need adjustment for windows
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
import random
import os
#import time # and time.sleep(0.017) windows??

win = turtle.Screen()
win.setup(800, 600)
win.bgcolor('grey')
win.title('Simple "Frogger" game with Python 3 and turtle with classes')
win.tracer(0)
win.listen()
pictures = ['car1.gif', 'car2.gif', 'car3.gif', 'car4.gif','car5.gif',
            'jump1.gif', 'jump2.gif', 'jump3.gif', 'jump4.gif', 'jump5.gif']
for i in pictures:
    win.register_shape(i)
    

class Frog(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.color('green')
        self.shapesize(2,2)
        self.s = 'jump1.gif'
        self.shape(self.s)
        self.goto(0, -220)
        self.jump = 'ready'

    def right(self):
        self.goto(self.xcor()+50, self.ycor())

    def left(self):
        self.goto(self.xcor()-50, self.ycor())



class Car(turtle.Turtle):
    def __init__(self, color, xpos, ypos, dx): # dx may need change in windows eg 0.05 instead of 2
        super().__init__(shape='square')
        self.shapesize(2,2)
        self.up()
        self.c = color
        self.color(self.c)
        self.ypos = ypos
        self.xpos = xpos
        self.goto(self.xpos, self.ypos)
        self.dx = dx

    def move(self):
        self.goto(self.xcor()+self.dx, self.ypos)
        


frog = Frog()
amount_enemies = 10

car_list1, car_list2, car_list3, car_list4, car_list5 = [], [], [], [], []
super_list = [car_list1, car_list2, car_list3, car_list4, car_list5]

# Will use y values to place our 5 rows of cars
y1 = 0
y2 = 180
y3 = 340
y4 = 560
y5 = 720

def frog_jump():
    global y1
    global y2
    global y3
    global y4
    global y5
    
    frog.jump = 'go'
    os.system('afplay jump.wav&')
    # Shift existing cars down
    for i in super_list:
        for j in i:
            j.ypos -= 30
            
    # Create new cars at the new y level to stay in line
    y1, y2, y3, y4,y5 = y1-30, y2-30, y3-30, y4-30, y5-30


win.onkey(frog_jump, 'Up')
win.onkey(frog.right, 'Right')
win.onkey(frog.left, 'Left')

counter = 0
game_over = False

while not game_over:
    win.update()
    #time.sleep(0.017) # windows?

    # Animate frog gif with jump
    if frog.jump == 'go':
        if frog.s == 'jump1.gif' and counter%5 == 0:
            frog.s = 'jump2.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump2.gif' and counter%5 == 0:
            frog.s = 'jump3.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump3.gif' and counter%5 == 0:
            frog.s = 'jump4.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump4.gif' and counter%5== 0:
            frog.s = 'jump1.gif'
            frog.shape(frog.s)
            frog.jump = 'ready'
        counter += 1
        
    for i in super_list:
        # Create new cars
        delay = random.random()
        if len(i)<amount_enemies and delay<0.01:
            if i == car_list1:
                car = Car('red', 440, y1, -2) 
                car.shape('car1.gif')
                car.list = i
                i.append(car)
            if i == car_list2:
                car = Car('blue', 440, y2, -2)
                car.shape('car2.gif')
                car.list = i
                i.append(car)
            if i == car_list3:
                car = Car('yellow', -440, y3, 2)
                car.shape('car3.gif')
                car.list = i
                i.append(car)
            if i == car_list4:
                car = Car('purple', -440, y4, 2)
                car.shape('car4.gif')
                car.list = i
                i.append(car)
            if i == car_list5:
                car = Car('green', -440, y5, 2)
                car.shape('car5.gif')
                car.list = i
                i.append(car)
            
        # Move cars over the screen
        for j in i:
            index = i.index(j)
            if i.index(j)==0: # Move first car immediately but wait with second to allow bit of distance
                j.move()
            elif i.index(j)>0 and j.distance(i[index-1])>= 110: # Allow better spacing of cars
                j.move()

            # Remove car if out of the screen
            if (j.xcor()<-400 and j.xpos>0) or (j.xcor()>400 and j.xpos<0):
                j.goto(1000,1000)
                j.list.remove(j)

            # shift row up 800 pixels if it goes below the screen
            if j.ycor()<-320:
                if j.ypos == y1:
                    y1 += 800
                if j.ypos == y2:
                    y2 += 800
                if j.ypos == y3:
                    y3 += 800
                if j.ypos == y4:
                    y4 += 800
                if j.ypos == y5:
                    y5 += 800

            if j.distance(frog)<50:
                game_over = True

frog.shape('jump5.gif')
frog.goto(0,0)
for i in super_list:
    for j in i:
        j.goto(1000,1000)
win.update()



