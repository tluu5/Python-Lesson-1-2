import math, random, turtle

#Base Utility Functions
def rnum(n0,n1): return random.randint(n0,n1)
def distForm(t1,t2): return math.sqrt((t2.xcor()-t1.xcor())**2+(t2.ycor()-t1.ycor())**2)
#Create Game Screen
screen = turtle.Screen()
screen.title('gameQuest1')
screen.bgcolor('black')
screen.screensize(1200,500); screen.setup(1250,550)

diff = int(screen.numinput('Game Difficulty','Please choose a difficulty between 1-10:',3,1,10))

#Create Player Turtle
player = turtle.Turtle()
player.penup()
player.shape('turtle')
player.color('green')
player.fillcolor('black')
player.speed(0)

#Game Borders
game_borders = {'min_x':-500,'max_x':500,'min_y':-230,'max_y':230}
def check_borders(t):
    if (t.xcor() < game_borders['min_x'] or t.xcor() > game_borders['max_x'] or 
        t.ycor() < game_borders['min_y'] or t.ycor() > game_borders['max_y']): 
        t.bk(25)

#Map Events (Key and click)
def move_forward(): player.forward(10); check_borders(player)
def move_backward(): player.backward(10); check_borders(player)
def turn_left(): player.left(15); check_borders(player)
def turn_right(): player.right(15); check_borders(player)

screen.onkeypress(move_forward,'w')
screen.onkeypress(move_backward,'s')
screen.onkeypress(turn_left,'a')
screen.onkeypress(turn_right,'d')

#Last 2 Lines ------
screen.listen()
screen.mainloop()