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


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('red')
        self.up()
        self.hideturtle()
        
        

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
        

class Game():
    def __init__(self):
        self.win = turtle.Screen()
        self.win.setup(800, 600)
        self.win.bgcolor('grey')
        self.win.title('Simple "Frogger" game with Python 3 and turtle with classes')
        self.win.tracer(0)
        self.win.listen()
        self.pictures = ['car1.gif', 'car2.gif', 'car3.gif', 'car4.gif','car5.gif',
                    'jump1.gif', 'jump2.gif', 'jump3.gif', 'jump4.gif', 'jump5.gif']
        for i in self.pictures:
            self.win.register_shape(i)

        self.pen = Scoreboard()


    def new_game(self):
        self.win.bgcolor('grey')
        self.pen.clear()
        
        self.frog = Frog()
        self.amount_enemies = 10

        self.car_list1, self.car_list2, self.car_list3, self.car_list4, self.car_list5 = [], [], [], [], []
        self.super_list = [self.car_list1, self.car_list2, self.car_list3, self.car_list4, self.car_list5]

        # Will use y values to place our 5 rows of cars
        self.y1 = 0
        self.y2 = 180
        self.y3 = 340
        self.y4 = 560
        self.y5 = 720
        self.counter = 0



        self.run()
        
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()



    def events(self):
        self.win.onkey(self.frog_jump, 'Up')
        self.win.onkey(self.frog.right, 'Right')
        self.win.onkey(self.frog.left, 'Left')



    def update(self):
        self.win.update()
        #time.sleep(0.017) # windows?

        # Animate frog gif with jump
        if self.frog.jump == 'go':
            if self.frog.s == 'jump1.gif' and self.counter%5 == 0:
                self.frog.s = 'jump2.gif'
                self.frog.shape(self.frog.s)
            elif self.frog.s == 'jump2.gif' and self.counter%5 == 0:
                self.frog.s = 'jump3.gif'
                self.frog.shape(self.frog.s)
            elif self.frog.s == 'jump3.gif' and self.counter%5 == 0:
                self.frog.s = 'jump4.gif'
                self.frog.shape(self.frog.s)
            elif self.frog.s == 'jump4.gif' and self.counter%5== 0:
                self.frog.s = 'jump1.gif'
                self.frog.shape(self.frog.s)
                self.frog.jump = 'ready'
            self.counter += 1
        
        for i in self.super_list:
            # Create new cars
            delay = random.random()
            if len(i)<self.amount_enemies and delay<0.01:
                if i == self.car_list1:
                    self.car = Car('red', 440, self.y1, -2) 
                    self.car.shape('car1.gif')
                    self.car.list = i
                    i.append(self.car)
                if i == self.car_list2:
                    self.car = Car('blue', 440, self.y2, -2)
                    self.car.shape('car2.gif')
                    self.car.list = i
                    i.append(self.car)
                if i == self.car_list3:
                    self.car = Car('yellow', -440, self.y3, 2)
                    self.car.shape('car3.gif')
                    self.car.list = i
                    i.append(self.car)
                if i == self.car_list4:
                    self.car = Car('purple', -440, self.y4, 2)
                    self.car.shape('car4.gif')
                    self.car.list = i
                    i.append(self.car)
                if i == self.car_list5:
                    self.car = Car('green', -440, self.y5, 2)
                    self.car.shape('car5.gif')
                    self.car.list = i
                    i.append(self.car)
            
            # Move cars accross the screen
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

                # shift row up 800 if below the screen
                if j.ycor()<-320:
                    if j.ypos == self.y1:
                        self.y1 += 800
                    if j.ypos == self.y2:
                        self.y2 += 800
                    if j.ypos == self.y3:
                        self.y3 += 800
                    if j.ypos == self.y4:
                        self.y4 += 800
                    if j.ypos == self.y5:
                        self.y5 += 800

                if j.distance(self.frog)<50:
                    self.playing = False



    def frog_jump(self):
    
        self.frog.jump = 'go'
        os.system('afplay jump.wav&')
        # Shift existing cars down
        for i in self.super_list:
            for j in i:
                j.ypos -= 30
            
        # Create new cars at the new y level to stay in line
        self.y1, self.y2, self.y3, self.y4,self.y5 = self.y1-30, self.y2-30, self.y3-30, self.y4-30, self.y5-30




    def show_start_screen(self):
        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('Simple Frogger Game using Python 3 and Turtle\n\n     Press the "space" key to continue',
                      align='center', font=('Courier', 24, 'normal'))
    


    def show_game_over_screen(self):
        
        self.frog.shape('jump5.gif')
        self.frog.goto(0,-150)
        for i in self.super_list:
            for j in i:
                j.goto(1000,1000)
        self.win.update()

        self.waiting = True
        self.pen.goto(0, 0)
        self.win.onkey(self.wait_for_keypress, 'space')
        
        while self.waiting:
            self.win.bgcolor('black')
            self.pen.write('\t   GAME OVER\n\n    Press "space" for new game',
                      align='center', font=('Courier', 24, 'normal'))

        self.frog.goto(1000,1000)


    def wait_for_keypress(self):
        self.waiting = False




game = Game()
game.show_start_screen()


while True:
    game.new_game()
    game.show_game_over_screen()
    
    
    




