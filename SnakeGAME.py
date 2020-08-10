import turtle
import time
import random

delay=0.1

#Score
score=0
high_score=0
#Set up the screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=700,height=700)
window.tracer(0)# turn offs the screen updates

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()#so that no line is drawn
head.goto(0,0)#to be in the center
head.direction="stop"

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()#so that no line is drawn
food.goto(0,100)#to be in the center

segments=[]

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Score: 0  High Score: 0", align="center",font=("Arial",24,"normal"))
#Functions
def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"
    
def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction !="left":
        head.direction="right"
    
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

        
#Keyboard Binding
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")


#Main Game Loop
while True:
    window.update()
    #Check for collision with border
    if head.xcor()>340 or head.xcor()<-340 or head.ycor()>340 or head.ycor()<-340:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        #Hide the Segments
        for segment in segments:
            segment.goto(1000,1000)
        #Clear the Segments
        segments.clear()

        #Reset the Score
        score = 0

        #Reset the delay
        delay = 0.1


        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))


    #Check for collision with food
    if head.distance(food) <20:
        #Move the food to random spot
        x=random.randint(-340,340)
        y=random.randint(-340,340)
        food.goto(x,y)

        #Add Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay -=0.001
        #Increase the Score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))

    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #Move segment 0 to where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    #Check for collision with body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide the segment
            for segment in segments:
                segment.goto(1000,1000)
            #Clear the segment
            segments.clear()
            #Reset the score
            score = 0
            #Reset the delay
            delay=0.1
            #Update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,high_score),align="center",font=("Arial",24,"normal"))
    time.sleep(delay)
window.mainloop()
