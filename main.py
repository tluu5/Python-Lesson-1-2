import os, sys, math, random, time, turtle


#Base Utility Functions
def rnum(n0, n1):
  return random.randint(n0, n1)


def distForm(t1, t2):
  return math.sqrt((t2.xcor() - t1.xcor())**2 + (t2.ycor() - t1.ycor())**2)


#Create Game Screen
screen = turtle.Screen()
screen.title('gameQuest1')
screen.bgcolor('black')
screen.screensize(1200, 500)
screen.setup(1250, 550)

diff = int(
    screen.numinput('Game Difficulty',
                    'Please choose a difficulty between 1-10:', 3, 1, 10))

#Create Player Turtle
player = turtle.Turtle()
player.penup()
player.shape('turtle')
player.color('green')
player.fillcolor('black')
player.speed(0)

#Game Borders
game_borders = {'min_x': -500, 'max_x': 500, 'min_y': -230, 'max_y': 230}


def check_borders(t):
  if (t.xcor() < game_borders['min_x'] or t.xcor() > game_borders['max_x']
      or t.ycor() < game_borders['min_y'] or t.ycor() > game_borders['max_y']):
    t.bk(25)


#Map Events (Key and click)
def move_forward():
  player.forward(10)
  check_borders(player)


def move_backward():
  player.backward(10)
  check_borders(player)


def turn_left():
  player.left(15)
  check_borders(player)


def turn_right():
  player.right(15)
  check_borders(player)


screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_backward, 's')
screen.onkeypress(turn_left, 'a')
screen.onkeypress(turn_right, 'd')

#Last 2 Lines ------
screen.listen()
screen.mainloop()

#Game Time
gameTime = 0
player_is_hurt = int(15 - diff)
lives = 3


def trackGameTime():

  global gameTime
  global player_is_hurt

  gameTime += 1
  player_is_hurt -= 1

  print('Time Alive:', gameTime, 'second(s) - Shield?:', player_is_hurt > 0)
  screen.ontimer(trackGameTime, 1000)


# Shield Visual Rep.
def toggleShield():
  if player_is_hurt > 0: player.fillcolor('blue')
  else: player.fillcolor('black')

  screen.ontimer(toggleShield, 5)


#food
food = turtle.Turtle()
food.penup()
food.hideturtle()
food.shape('square')
food.color('green')


def spawn_food():
  global lives
  if food.isvisible():
    if distForm(food, player) <= 25:
      food.hideturtle()
      lives += 1
      print('EXTRA LIFE! -- Now you have', lives)
    screen.ontimer(spawn_food, 10)
  else:
    food.setpos(rnum(-450, 450), rnum(-200, 200))
    food.showturtle()
    screen.ontimer(spawn_food, rnum(10 * diff, 1000 * diff))


#Enemies
enemies = []
lives = 3

for i in range(diff * 10):
  enemies.append(turtle.Turtle())
  enemies[-1].hideturtle()
  enemies[-1].penup()
  enemies[-1].shape('turtle')
  enemies[-1].color('red')
  enemies[-1].speed(0 if diff == 10 else int(diff + 1))
  enemies[-1].setpos(rnum(-450, 450), rnum(-200, 200))

for et in enemies:
  et.showturtle()


def moveEnemies():
  global enemies
  global lives
  global player_is_hurt

  for e in enemies:
    e.fd(rnum(2 * diff, 5 * diff))
    check_borders(e)

    if distForm(e, player) <= 50 and e.isvisible() and player_is_hurt <= 0:
      player_is_hurt = int(11 - diff)
      lives -= 1

      if lives <= 0:
        print('You lose -- you lasted:', gameTime, 'second(s')
        screen.bye()

      else:
        print('You got hit!!! You have', lives, 'lives left!')

      e.hideturtle()
      e.setpos(rnum(-450, 450), rnum(-200, 200))
      e.showturtle()

    if rnum(1, 100) > 80: e.rt(180)
    else: e.rt(rnum(-25, 25))

  screen.ontimer(moveEnemies, 10)
