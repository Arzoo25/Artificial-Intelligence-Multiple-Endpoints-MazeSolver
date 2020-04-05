import turtle                    # import turtle library
import time
import sys
from collections import deque

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("Path Finder")
wn.setup(1300,700)                  # setup the dimensions of the working window

class Maze(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    def __hash__(self):               #<-- added a hash method
        return hash(self.position)

grid1 = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
"+s          +                 +               ++  +",
"+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
"+  +     +  +           +  +                 +++  +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
"+  +  +  +  +  +  +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +     +  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+ e                     +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

def maze_outline(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            character = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "+":
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            if character == " " or character == "e":
                path.append((screen_x, screen_y))

            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x,screen_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()
    
def DFS(x,y):
    stack.append((x, y))
    solution[x,y] = x,y

    while len(stack) > 0:
        time.sleep(0)
        x, y = stack.pop()
        if (x,y) == (end_x,end_y):
            break
        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            solution[cell] = x, y
            stack.append(cell)   
            visited.add((x-24, y))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            solution[cell] = x, y
            stack.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            solution[cell] = x, y
            stack.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            solution[cell] = x, y
            stack.append(cell)
            visited.add((x, y + 24))
        green.goto(x,y)
        green.stamp()
        
def backRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (start_x, start_y):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]
        
maze = Maze()
red = Red()
green = Green()
yellow = Yellow()

walls = []
path = []
visited = set()
stack = []
solution = {}

maze_outline(grid1) 
start_time = time.time()
DFS(start_x,start_y)
print((time.time() - start_time))
backRoute(end_x, end_y)
wn.exitonclick()
