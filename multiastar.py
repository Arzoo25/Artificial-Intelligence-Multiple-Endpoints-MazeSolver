# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 05:10:35 2020

@author: Rohit
"""

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
                green.color("purple")
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

def astar(start_x, start_y, end_x, end_y):
    start_node = Node(None, (start_x,start_y))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, (end_x,end_y))
    end_node.g = end_node.h = end_node.f = 0
    open_list = []
    closed_list = set()
    open_list.append(start_node)
    while len(open_list) > 0:
        current_node = open_list[0]
        time.sleep(0)
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        open_list.pop(current_index)
        closed_list.add(current_node)
        if current_node == end_node:
            current = current_node
            while current is not None:
                track.append(current.position)
                current = current.parent
            return track[::-1]
        green.goto(current_node.position)
        green.stamp()
        children = []
        for new_position in [(0, -24), (0, 24), (-24, 0), (24, 0), (-24, -24), (-24, 24), (24, -24), (24, 24)]: # Adjacent squares
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position in walls:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:
            if child in closed_list:
                continue
            child.g = current_node.g + 24
            child.h = ((child.position[0] - end_node.position[0])**2)+ ((child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)
            red.goto(child.position)
            red.stamp()

maze = Maze()
red = Red()
green = Green()
yellow = Yellow()

walls = []
path = []
frontier = deque()
paths = []
solution = {}
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
    track = []
    astar(start_x,start_y, x[0],x[1])
    solutions.append(track)
    start_x = x[0]
    start_y = x[1]
print((time.time() - start_time))
solutions = [ele for ele in reversed(solutions)]
endnew = [ele for ele in reversed(endnew)]
def astarRoute(x, y,end_x, end_y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (end_x, end_y):
        x, y =paths.pop()
        yellow.goto((x, y))
        yellow.stamp()
for x in start:
    y = endnew.pop()
    paths = solutions.pop()
    astarRoute(x[0], x[1], y[0], y[1])
wn.exitonclick()
