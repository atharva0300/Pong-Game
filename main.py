#Simple Pong Game 
#Part 1 : Getting Started

import turtle 
import winsound

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width= 800 , height = 600)
wn.tracer(0)


# Creating Scores
score_a = 0
score_b = 0
# We'll get the score when the score goes to the right sode 
# either + or - right 

# Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350 ,0)

# Paddle B 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350 ,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =1  # Change the x cordinate by 2 pixels
ball.dy = 1     # Changes the y cordinate by 2 pixels

# scoring section
# score
score  = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: {0} Player B: {1}" .format(score_a,score_b) , align="center" , font=("Courier" , 24, "normal"))

#Function 
# Moving paddle_a and paddle_b up and down
def paddle_a_up(): 
    y = paddle_a.ycor()
    # Returns the y cordinate 
    # y incraess when it goes up 
    # so ,
    y =y+20  # increases the value of y by 20 
    paddle_a.sety(y)    # sets the ew value of y

def paddle_a_down(): 
    y = paddle_a.ycor()
    # Returns the y cordinate 
    # y incraess when it goes up 
    # so ,
    y =y-20  # increases the value of y by 20 
    paddle_a.sety(y)    # sets the ew value of y

def paddle_b_up(): 
    y = paddle_b.ycor()
    # Returns the y cordinate 
    # y incraess when it goes up 
    # so ,
    y =y+20  # increases the value of y by 20 
    paddle_b.sety(y)    # sets the ew value of y

def paddle_b_down(): 
    y = paddle_b.ycor()
    # Returns the y cordinate 
    # y incraess when it goes up 
    # so ,
    y =y-20  # increases the value of y by 20 
    paddle_b.sety(y)    # sets the ew value of y

# Keyboard Binding 
wn.listen() # Listens the keyboard input 
wn.onkeypress(paddle_a_up , "w")    # Calls the fuction paddle_a_up 
# when w is called 
# and increase the value of y by 20 ( in the paddle_a_up function)

# Keyboard Binding 
#wn.listen() # Listens the keyboard input 
wn.onkeypress(paddle_a_down, "s")    # Calls the fuction paddle_a_down 
# when s is called 
# and decreases the value of y by 20 ( in the paddle_a_down function)

wn.onkeypress(paddle_b_up , "Up")    # Calls the fuction paddle_a_up 
# when w is called 
# and increase the value of y by 20 ( in the paddle_a_up function)

# Keyboard Binding 
#wn.listen() # Listens the keyboard input 
wn.onkeypress(paddle_b_down, "Down")    # Calls the fuction paddle_a_down 
# when s is called 
# and decreases the value of y by 20 ( in the paddle_a_down function)




# Main game loop
while True: 
    wn.update()

    # Move the ball 
    ball.setx(ball.xcor() + ball.dx)    # Set the x cordinate of x 
    # at current x cordinate of x function() + the change in the distance of x ( dx = 2 )
    ball.sety(ball.ycor()  + ball.dy)
    # Set the x cordinate of y
    # at current y cordinate of y function() + the change in the distance of y ( dy = 2 )


    # Ball checking 
    # Top and bottom border 
    if ball.ycor()>300: 
        ball.sety(300)  # Set y at 290
        ball.dy = ball.dy*(-1)

    if ball.ycor()<-300: 
        ball.sety(-300)  # Set y at 290
        ball.dy = ball.dy*(-1)
    
    # Ball cHECKIGN LEFT and right border 
    if ball.xcor()>400: 
        ball.goto(0,0)    # move the ball to 0,0
        ball.dx = ball.dx*(-1)
        score_a = score_a+1
        score.clear()
        score.write("Player A: {0} Player B: {1}" .format(score_a,score_b) , align="center" , font=("Courier" , 24, "normal"))
    
    if ball.xcor()<-400: 
        ball.goto(0,0)    # move the ball to 0,0
        ball.dx = ball.dx*(-1)
        score_b=score_b+1
        score.clear()
        score.write("Player A: {0} Player B: {1}" .format(score_a,score_b) , align="center" , font=("Courier" , 24, "normal"))

    # gettig the right paddle working 
    # padlle and ball collision
    if (ball.xcor() > 340) and (ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50) and (ball.ycor() > paddle_b.ycor()-50): 
        ball.setx(340)
        ball.dx = ball.dx*(-1)
        winsound.PlaySound("Pong_sound.wav", winsound.SND_ASYNC)
        

    if (ball.xcor() < -340) and (ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50) and (ball.ycor() > paddle_a.ycor()-50): 
        ball.setx(-340)
        ball.dx = ball.dx*(-1)
        winsound.PlaySound("Pong_sound.wav", winsound.SND_ASYNC)
        
    

#End