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

picture_files = ['jump1.gif', 'jump2.gif', 'jump3.gif', 'jump4.gif', 'jump5.gif',
                 'car1.gif', 'car2.gif', 'car3.gif', 'car4.gif', 'car5.gif']

for i in picture_files:
    win.register_shape(i) 


pen = turtle.Turtle()
pen.hideturtle()
pen.up()
pen.goto(0, 250)
pen.color('red')
pen.write('"Frogger" Pyton 3 and Turtle', align='center', font=('Courier', 24, 'normal'))

frog = turtle.Turtle()
frog.s = 'jump1.gif'
frog.shape(frog.s)
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
car_list5 = []
super_list = [car_list, car_list2, car_list3, car_list4, car_list5]  # This will help reduce repitition

amount_cars = 10

yvalue1 = 0
yvalue2 = 180
yvalue3 = 340
yvalue4 = 560
yvalue5 = 720

def running_cars():
    global shifting_yaxis # not a local variable for the function only
    
    global yvalue1
    global yvalue2
    global yvalue3
    global yvalue4
    global yvalue5
   
    delay = random.random()  # Creates a probability of making a new car
    
    for i in super_list:
        delay = random.random()
        
        if len(i) < amount_cars and delay < 0.01:
            car = turtle.Turtle()
            car.shapesize(2,2)
            car.up()
            car.list = i
            if car.list == car_list:    
                car.shape('car1.gif')
                car.dx = -2
                car.y = yvalue1
                car.color('red')
                car.goto(440, shifting_yaxis + car.y) # shifting axis will change with jumps
                
            elif car.list == car_list2:
                car.shape('car2.gif')
                car.dx = -2
                car.y = yvalue2
                car.color('blue')
                car.goto(440, shifting_yaxis + car.y) # shifting axis will change with jumps
            elif car.list == car_list3:
                car.shape('car3.gif')
                car.dx = 2
                car.y = yvalue3
                car.color('yellow')
                car.goto(-440, shifting_yaxis + car.y) 
            elif car.list == car_list4:
                car.shape('car4.gif')
                car.dx = 2
                car.y = yvalue4
                car.color('green')
                car.goto(-440, shifting_yaxis + car.y)
            elif car.list == car_list5:
                car.shape('car5.gif')
                car.dx = 2
                car.y = yvalue5
                car.color('green')
                car.goto(-440, shifting_yaxis + car.y)
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
    global yvalue5
    
    for i in super_list: # For the list in superlist
        for j in i: # for each car in the list
            indx = i.index(j) # Index position of this car
            if i.index(j)==0: # First car in list - move
                j.goto(j.xcor()+ j.dx, j.ycor())
            # Try to space out a little bit    
            elif indx > 0 and j.distance(i[indx-1]) > 110:
                j.goto(j.xcor()+ j.dx, j.ycor())
            
            # Remove from list if out left or right side of screen
            if j.xcor() < -420 and j.dx == -2:
                j.goto(1000,1000)
                j.list.remove(j)
            elif j.xcor()>420 and j.dx == 2:
                j.goto(1000,1000)
                j.list.remove(j)

            # Clear list and move 800 pixels up if below the screen  
            if j.ycor()<-320:
                if j.y == yvalue1:
                    yvalue1 += 800 # Move whole row up 800 pixels
                elif j.y == yvalue2:
                    yvalue2 += 800
                elif j.y == yvalue3:
                    yvalue3 += 800
                elif j.y == yvalue4:
                    yvalue4 += 800
                elif j.y == yvalue5:
                    yvalue5 += 800
                
           
def collision_check():
    global game_over

    for i in super_list:
        for j in i:
            if j.distance(frog)<60:
                game_over = True
            
            
            
win.listen()
win.onkey(move_left, 'Left')
win.onkey(move_right, 'Right')
win.onkey(jump, 'Up')


counter = 1

while not game_over:
    win.update()
    #time.sleep(0.017) # windows?
    
    if counter%20 == 0:
        running_cars()
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


# Game over

for i in super_list:
    for j in i:
        j.goto(1000,1000)
frog.shape('jump5.gif')
win.update() # needed due to win.tracer(0) to change to new gif
pen.goto(0,0)
pen.write('GAME OVER', align='center', font=('Courier', 36, 'normal'))





