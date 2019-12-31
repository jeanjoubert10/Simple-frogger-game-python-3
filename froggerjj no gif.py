# Simple frogger type game J Joubert 24 Oct 2019
# Python 3 with Turtle module on mac
# Sounds only for mac using afplay
# winsound for windows
# This code can be copied, changed, updated and if improved - please let me know how!!

import turtle
import random
import os
#import time # and time.sleep(0.017) windows??

win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('grey')
win.title('Simple "Frogger" with Python 3 and Turtle')
win.tracer(0)   # Stops animation until win.update() - try game without this

pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.goto(0, 250)
pen.color('black')
pen.write('"Frogger" Pyton 3 and Turtle', align='center', font=('Courier', 24, 'normal'))

frog = turtle.Turtle()
frog.shape('square')
frog.color('green')
frog.up()
frog.speed(0)
frog.shapesize(2,2)
frog.goto(0, -130)
frog.jump = 'ready'

game_over = False
shifting_yaxis = 0  # Everything needs to shift down with every jump - this is the reference

car_list, car_list2, car_list3, car_list4 = [], [], [], []
super_list = [car_list, car_list2, car_list3, car_list4]  # This will help reduce repitition

amount_cars = 12 # 12 in each list

# Initial y values - will add 800 everytime it goes below the screen
yvalue1 = 0
yvalue2 = 180
yvalue3 = 340
yvalue4 = 560

def running_cars():
    global shifting_yaxis # not a local variable for the function only
    
    global yvalue1
    global yvalue2
    global yvalue3
    global yvalue4
    
    for i in super_list:
        delay = random.random() # Creates random delay (probability 0 - 1)
        
        if len(i) < amount_cars and delay < 0.02: # Can play around with delay threshold
            car = turtle.Turtle()
            car.shape('square')
            car.shapesize(2,2)
            car.up()
            car.list = i
            if car.list == car_list:
                car.dx = -2
                car.y = yvalue1
                car.color('red')
                car.goto(420, shifting_yaxis + car.y) # shifting axis will change with jumps
            elif car.list == car_list2:
                car.dx = -2
                car.y = yvalue2
                car.color('blue')
                car.goto(420, shifting_yaxis + car.y) # shifting axis will change with jumps
            elif car.list == car_list3:
                car.dx = 2
                car.y = yvalue3
                car.color('yellow')
                car.goto(-420, shifting_yaxis + car.y) # shifting axis will change with jumps
            elif car.list == car_list4:
                car.dx = 2
                car.y = yvalue4
                car.color('green')
                car.goto(-420, shifting_yaxis + car.y) # shifting axis will change with jumps
            i.append(car)
        

def move_left():
    if frog.xcor()>-360: # Move left only if still in the screen
        frog.setx(frog.xcor()-40)


def move_right():
    if frog.xcor()<= 340:
        frog.setx(frog.xcor()+40)


def jump():
    global shifting_yaxis # not a local variable for the function only
    
    frog.jump = 'go'
    shifting_yaxis -= 30
    os.system('afplay jump.wav&')
    
    for i in super_list:  # Shift all cars in all 4 lists down with 30 pixels
        for j in i:    
            j.goto(j.xcor(), shifting_yaxis + j.y)
            

def move_cars():  # Values may have to be adjusted in windows eg 0.02 instead of 2????
    global yvalue1
    global yvalue2
    global yvalue3
    global yvalue4
    
    for i in super_list: # For the list in superlist
        for j in i: # for each car in the list

            # Move cars left or right
            j.goto(j.xcor()+ j.dx, j.ycor())

            # If car is out screen left or right, remove from list
            if j.xcor() < -420 and j.dx == -2: 
                j.goto(1000,1000)
                j.list.remove(j)
            elif j.xcor()>420 and j.dx == 2:
                j.goto(1000,1000)
                j.list.remove(j)

            # If cars go below the screen, reset that list 800 pixels higher    
            if j.ycor()<-320:
                if j.y == yvalue1:
                    yvalue1 += 800
                elif j.y == yvalue2:
                    yvalue2 += 800 
                elif j.y == yvalue3:
                    yvalue3 += 800
                elif j.y == yvalue4:
                    yvalue4 += 800
                   
           
def collision_check():
    global game_over # game_over variable from outside this function

    for i in super_list:
        for j in i:
            if j.distance(frog)<50:
                game_over = True
            
            
            
win.listen()
win.onkey(move_left, 'Left')
win.onkey(move_right, 'Right')
win.onkey(jump, 'Up')


while not game_over:
    win.update()
    #time.sleep(0.017) # windows?
    
    running_cars()
    move_cars()
    collision_check()

win.update() # needed due to win.tracer(0) 
pen.goto(0,0)
pen.write('GAME OVER', align='center', font=('Courier', 36, 'normal'))





