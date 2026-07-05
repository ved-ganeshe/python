import turtle
screen = turtle.Screen()
screen.bgcolor('white')
screen.setup(width = 600, height = 600)
turtle.shape('arrow')
turtle.speed(100)
maze = [
    "XXXXXXXXXXXXXXX",
    "X             X",
    "X XXXXX XXXXX X",
    "X X     X     X",
    "X X XXX X XXX X",
    "X X   X X X   X",
    "X XXX X X X X X",
    "X     X X X  XX",
    "XXXXX X X X XXX",
    "X     X   X  XX",
    "XXXXXXX XXXXXXX",
    "X             ",
    "XXXXXXXXXXXXX F"
]
player = turtle.Turtle()
player.shape('arrow')
player.color('blue')
player.penup()
player.speed(0)
obstacles = []
def create_maze():
    global finish_line
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]
            screen_x = -288+(x * 24) 
            screen_y = 288 - (y * 24)
            if character == "X":
                obstacle = turtle.Turtle()
                obstacle.shape("square")
                obstacle.color("black")
                obstacle.pu()
                obstacle.goto(screen_x, screen_y)
                obstacles.append(obstacle)
            elif character == "F":
                finish_line = turtle.Turtle()
                finish_line.shape("circle")
                finish_line.color("green")
                finish_line.pu()
                finish_line.goto(screen_x, screen_y)

def is_valid_move(x, y):
    for obstacle in obstacles:
        if abs(obstacle.xcor() - x) < 20 and abs(obstacle.ycor() - y) < 20:
            return False
    return True

def check_win():
    if abs(player.xcor() - finish_line.xcor()) < 20 and abs(player.ycor() - finish_line.ycor()) < 20:
        print("You won!")

def move_up():
    new_x = player.xcor()
    new_y = player.ycor() + 24
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
        check_win()

def move_down():
    new_x = player.xcor()
    new_y = player.ycor() - 24
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
        check_win()

def move_left():
    new_x = player.xcor() - 24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
        check_win()

def move_right():
    new_x = player.xcor() + 24
    new_y = player.ycor()
    if is_valid_move(new_x, new_y):
        player.goto(new_x, new_y)
        check_win()

create_maze()
player.goto(-288, 288)
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.listen()
turtle.done()