import turtle
import random
import time
import pygame
turtle.penup()
turtle.tracer(1,0)
turtle.goto(-300, 0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 5
START_LENGTH = 4
TIME_STEP = 10
time_count = turtle.clone()
time_count.penup()
time_count.goto(0, 0)
food_pos = []
food_stamps = []

turtle.direction = "Up"

player_status = "alive"
UP_EDGE = 250
DOWN_EDGE = -250


turtle.register_shape("1.gif")
turtle.register_shape("2.gif")
turtle.register_shape("3.gif")


turtle.register_shape("seaturtle_1.gif")
turtle.register_shape("seaturtle_2.gif")
turtle.register_shape("seaturtle_3.gif")
turtle.register_shape("seaturtle_4.gif")
turtle.register_shape("seaturtle_5.gif")
turtle.register_shape("seaturtle_6.gif")
turtle.register_shape("seaturtle_7.gif")
turtle.register_shape("seaturtle_8.gif")
turtle.register_shape("seaturtle_9.gif")
turtle.register_shape("seaturtle_10.gif")
turtle.register_shape("seaturtle_11.gif")
turtle.register_shape("seaturtle_12.gif")
turtle.register_shape("seaturtle_13.gif")
turtle.register_shape("seaturtle_14.gif")
turtle.register_shape("seaturtle_15.gif")
turtle.register_shape("seaturtle_16.gif")
turtle.register_shape("seaturtle_17.gif")
turtle.register_shape("seaturtle_18.gif")
turtle.register_shape("seaturtle_19.gif")
turtle.register_shape("seaturtle_20.gif")
turtle.register_shape("seaturtle_21.gif")
turtle.register_shape("seaturtle_22.gif")
turtle.register_shape("seaturtle_23.gif")
turtle.register_shape("seaturtle_24.gif")
turtle.register_shape("seaturtle_25.gif")
turtle.register_shape("seaturtle_26.gif")
turtle.register_shape("seaturtle_27.gif")
turtle.register_shape("seaturtle_28.gif")


turtle.shape("seaturtle_1.gif")

def up():
    turtle.direction="Up" #Change direction to up
    print("You pressed the up key!")

def down():
    turtle.direction="Down"
    print("You pressed the down key!")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.listen()

def turtle_animation() :
        while player_status == "alive":
            turtle.shape("seaturtle_1.gif")      
            time.sleep(0.0257)
            turtle.shape("seaturtle_1.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_2.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_3.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_4.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_5.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_6.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_7.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_8.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_9.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_10.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_11.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_12.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_13.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_14.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_15.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_16.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_17.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_18.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_19.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_20.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_21.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_22.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_23.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_24.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_25.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_26.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_27.gif")
            time.sleep(0.0257)
            turtle.shape("seaturtle_28.gif")
            

def move_turtle():
    
    my_pos = turtle.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if turtle.direction == "Up":
        turtle.goto(x_pos, y_pos + SQUARE_SIZE)
    elif turtle.direction=="Down":
        turtle.goto(x_pos, y_pos - SQUARE_SIZE)



    if y_pos >= UP_EDGE:
        print("You hit the UP EDGE! Game over!")
        quit()
    elif  DOWN_EDGE >= y_pos :
        print("You hit the DOWN EDGE! Game over!")
        quit()

    
   
     
         
    turtle.ontimer(move_turtle,TIME_STEP)

    

    
 
time_count.shape("1.gif")
time.sleep(1)
time_count.shape("2.gif")
time.sleep(1)
time_count.shape("3.gif")
time.sleep(1)
time_count.hideturtle()
move_turtle()
turtle_animation()
turtle.mainloop()
