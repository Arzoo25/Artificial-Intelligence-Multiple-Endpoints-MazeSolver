import turtle                    # import turtle library
import time
import sys
from collections import deque


choice = int(input("BFS-1,DFS-2,A star-3:"))
grid_Choice = int(input("grid choice 1-3:"))
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
"+  +++++++                                        +",
"+  +                    +  +                 +++  +",
"+             +   ++++  +  +  +++++++++++++  +++  +",
"+  +  +           +        +  +  +        +       +",
"+  +  ++++  +  ++++++++++ e+  +  ++++  +  +  ++   +",
"+  +     +  +          +   +           +  +  ++  ++",
"+  ++++  +                    +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +                          ++++++++++  +++  +",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++                                    +   +",
"+  +                    +  +  +     +     +  ++  ++",
"+  +  +                          ++++++++++  ++  ++",
"+ e                     +  +  +              ++  ++",
"+ ++++++                                   e+++  ++",
"+ ++++++                                         ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

grid2 = [
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
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++   e+++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

grid3 = [
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
"+               +                                 +",
"+                                                 +",
"+s          +                 +               ++  +",
"+                          +                      +",
"+                       +  +                 +++  +",
"+                 ++++  +  +  +++++++++++++  +++  +",
"+                 +        +  +  +        +       +",
"+              ++++++++++  +  +  ++++  +  +  ++   +",
"+                      +   +           +  +  ++  ++",
"+                             +++++++++++++  ++  ++",
"+     +  +     +              +              ++   +",
"++++  +                                          e+",
"+  +  +                    +     +     +  +  +++  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
"+  +  +     +     +     +  +  +     +    e+  ++  ++",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
"+                       +  +  +              ++  ++",
"+ ++++++             +  +  +  +  +++        +++  ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
"+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
"+      ++ +++++++++++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def setup_maze(grid):
    global start_x, start_y
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
                green.goto(screen_x, screen_y)
                end.append((screen_x,screen_y))
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def BFS(x,y,end_x,end_y):
    frontier.append((x,y))
    result = {}
    result[x,y] = x,y

    while len(frontier) > 0:
        time.sleep(0)
        distance = {}
        x, y = frontier.popleft()
        if(x - 24, y) in path and (x - 24, y) not in visited:
            cell = (x - 24, y)
            result[cell] = x, y
            distance[cell] =  abs(x-24 - end_x)+abs(y  -end_y)
            visited.add((x-24, y))
        
        if(x - 24, y + 24) in path and (x - 24, y + 24) not in visited:
            cell = (x - 24, y + 24)
            result[cell] = x, y
            distance[cell] =  abs(x-24 - end_x)+abs(y + 24  -end_y)
            visited.add((x-24, y + 24))
            
        if(x + 24, y + 24) in path and (x + 24, y + 24) not in visited:
            cell = (x + 24, y + 24)
            result[cell] = x, y
            distance[cell] =  abs(x+24 - end_x)+abs(y + 24  -end_y)
            visited.add((x+24, y+24))
        
        if(x - 24, y - 24) in path and (x - 24, y - 24) not in visited:
            cell = (x - 24, y - 24)
            result[cell] = x, y
            distance[cell] =  abs(x-24 - end_x)+abs(y - 24  -end_y)
            visited.add((x-24, y - 24))
        
        if(x + 24, y - 24) in path and (x + 24, y - 24) not in visited:
            cell = (x + 24, y - 24)
            result[cell] = x, y
            distance[cell] =  abs(x+24 - end_x)+abs(y - 24 -end_y)
            visited.add((x+24, y - 24))

        if (x, y - 24) in path and (x, y - 24) not in visited:
            cell = (x, y - 24)
            result[cell] = x, y
            distance[cell] =  abs(x - end_x)+abs(y - 24  -end_y)
            visited.add((x, y - 24))

        if(x + 24, y) in path and (x + 24, y) not in visited:
            cell = (x + 24, y)
            result[cell] = x, y
            distance[cell] =  abs(x + 24 - end_x)+abs(y  -end_y)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:
            cell = (x, y + 24)
            result[cell] = x, y
            distance[cell] =  abs(x - end_x)+abs(y + 24 -end_y)
            visited.add((x, y + 24))
        sorteddict = sorted(distance.items())
        for xy in sorteddict:
            frontier.append(xy[0])
        green.goto(x,y)
        green.stamp()
        if (x,y) == (end_x,end_y):
            break
    return result

maze = Maze()
red = Red()
green = Green()
yellow = Yellow()

walls = []
path = []

stack = []
solution = {}
track = []
end = []
solutions = []
setup_maze(grid3)
start = []
dicti = {}
mandist = []
for x  in end:
    dist = abs(start_x - x[0])+abs(start_y  - x[1])
    dicti[x] = dist
    mandist.append(dist)
mandist.sort()
sortdict = sorted(dicti.items())
endnew=[]
for x in sortdict:
    endnew.append(x[0])
start_time = time.time()
for x in endnew:
    start.append((start_x,start_y))
    visited = set()
    frontier = deque()
    solutions.append(BFS(start_x,start_y, x[0],x[1]))
    start_x = x[0]
    start_y = x[1]
print((time.time() - start_time))
def backRoute(x, y,startx,starty):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (startx,starty):
        yellow.goto(solution[x, y])
        yellow.stamp()
        x, y = solution[x, y]
for x in [ele for ele in reversed(start)]:
    y = endnew.pop()
    solution = solutions.pop()
    backRoute(y[0], y[1], x[0], x[1])
wn.exitonclick()


    