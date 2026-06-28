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
    "X XXX X X X XXX",
    "X     X X XXXXX",
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
            screen_y = 288 - (y * 4)
            if character == "X":
                obstacle = turtle.Turtle()
                obstacle.shape("square")
                obstacle.color("black")
                obstacle.pu()
                obstacle.goto(screen_x, screen_y)
            elif character == "F":
                finish_line = turtle.Turtle()
                finish_line.shape("circle")
                finish_line.color("green")
                finish_line.pu()
                finish_line.goto(screen_x, screen_y)
def move_up():
    new_x = player.xcor
    new_y = player.ycor + 24 
turtle.done()