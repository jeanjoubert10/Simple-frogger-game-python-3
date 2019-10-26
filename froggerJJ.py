# Simple frogger type game J Joubert 24 Oct 2019
# Python 3 with Turtle module on mac
# Sounds only for mac using afplay
# winsound for windows

import turtle
import random
import os

win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('grey')
win.title('Simple "Frogger" with Python 3 and Turtle')
win.tracer(0)   # Stops animation until win.update() - try game without this
win.register_shape('jump1.gif') 
win.register_shape('jump2.gif')
win.register_shape('jump3.gif')
win.register_shape('jump4.gif')
win.register_shape('jump5.gif')

pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.goto(0, 250)
pen.color('black')
pen.write('"Frogger" Pyton 3 and Turtle', align='center', font=('Courier', 24, 'normal'))

frog = turtle.Turtle()
frog.s = 'jump1.gif'
frog.shape(frog.s)
#frog.color('green')
frog.up()
frog.speed(0)
frog.shapesize(2,2)
frog.goto(0, -130)
frog.jump = 'ready'

game_over = False
shifting_yaxis = 0  # Everything needs to shift down with every jump - this is the reference

car_list = []
car_list2 = []
car_list3 = []
car_list4 = []

amount_cars = 12

new_line = 0    # start ycor() value for the row of cars
new_line2 = 180
new_line3 = 340
new_line4 = 520

def running_cars():
    # Same code x4 (for 4 rows of cars)
    # There must be a better way... 
    
    global shifting_yaxis # not a local variable for the function only
    
    delay = random.random()  # Creates a probability of making a new car
    if len(car_list) < amount_cars and delay < 0.02:
        car = turtle.Turtle()
        car.shape('square')
        car.shapesize(2,2)
        car.color('red')
        car.up()
        car.goto(420, shifting_yaxis + new_line) # shifting axis will change with jumps
        car_list.append(car)
        
    delay2 = random.random()
    if len(car_list2) < amount_cars and delay2 < 0.02:
        car = turtle.Turtle()
        car.shape('square')
        car.shapesize(2,2)
        car.color('blue')
        car.up()
        car.goto(420, shifting_yaxis + new_line2)
        car_list2.append(car)

    delay3 = random.random()
    if len(car_list3) < amount_cars and delay3 < 0.02:
        car = turtle.Turtle()
        car.shape('square')
        car.shapesize(2,2)
        car.color('yellow')
        car.up()
        car.goto(-420, shifting_yaxis + new_line3)
        car_list3.append(car)

    delay4 = random.random()
    if len(car_list4) < amount_cars and delay4 < 0.02:
        car = turtle.Turtle()
        car.shape('square')
        car.shapesize(2,2)
        car.color('green')
        car.up()
        car.goto(-420, shifting_yaxis + new_line4)
        car_list4.append(car)



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

    # Shift all 4 rows of cars down to the new shifting_yaxis reference
    for i in car_list:
        i.goto(i.xcor(),shifting_yaxis + new_line)

    for i in car_list2:
        i.goto(i.xcor(),shifting_yaxis + new_line2)

    for i in car_list3:
        i.goto(i.xcor(),shifting_yaxis + new_line3)

    for i in car_list4:
        i.goto(i.xcor(), shifting_yaxis + new_line4)


def move_cars():  # Values may have to be adjusted in windows eg 0.02 instead of 2????
    global new_line
    global new_line2
    global new_line3
    global new_line4

    # Repeat code 4x for the 4 rows of cars
    for i in car_list:
        i.goto(i.xcor()-2, i.ycor())
        if i.xcor()<-400:       # If car goes out on the left
            i.goto(1000,1000)
            car_list.remove(i)
            
        if i.ycor() <-320:      # If car goes below the screen
            new_line += 800
            car_list.clear()

    for i in car_list2:
        i.goto(i.xcor()-2, i.ycor())
        if i.xcor()<-400:
            i.goto(1000,1000)
            car_list2.remove(i)
            
        if i.ycor()<-320:
            new_line2 += 800
            car_list2.clear()

    for i in car_list3:
        i.goto(i.xcor()+2, i.ycor())
        if i.xcor() > 400:
            i.goto(1000,1000)
            car_list3.remove(i)
            
        if i.ycor()<-320:
            new_line3 += 800
            car_list3.clear()

    for i in car_list4:
        i.goto(i.xcor()+2, i.ycor())
        if i.xcor() > 400:
            i.goto(1000,1000)
            car_list4.remove(i)
            
        if i.ycor()<-320:
            new_line4 += 800
            car_list4.clear()
            
def collision_check():
    global game_over

    # Repeat code 4x for the 4 rows of cars
    for i in car_list:
        if i.distance(frog)<50:
            game_over = True
            

    for i in car_list2:
        if i.distance(frog)<50:
            game_over = True
            

    for i in car_list3:
        if i.distance(frog)<50:
            game_over = True

    for i in car_list4:
        if i.distance(frog)<50:
            game_over = True
            
            
win.listen()
win.onkey(move_left, 'Left')
win.onkey(move_right, 'Right')
win.onkey(jump, 'Up')


counter = 1

while not game_over:
    win.update()
    running_cars()
    move_cars()
    collision_check()

    if frog.jump == 'go':
        if frog.s == 'jump1.gif' and counter%5 == 0: # Change picture every 5th time in the loop
            frog.s = 'jump2.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump2.gif' and counter%5 == 0:
            frog.s = 'jump3.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump3.gif' and counter%5 == 0:
            frog.s = 'jump4.gif'
            frog.shape(frog.s)
        elif frog.s == 'jump4.gif' and counter%5 == 0:
            frog.s = 'jump1.gif'
            frog.shape(frog.s)
            frog.jump = 'ready'
            
        counter += 1


frog.shape('jump5.gif')
win.update() # needed due to win.tracer(0) to change to new gif
pen.goto(0,0)
pen.write('GAME OVER', align='center', font=('Courier', 36, 'normal'))





