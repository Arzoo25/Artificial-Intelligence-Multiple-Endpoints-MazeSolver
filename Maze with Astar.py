# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 12:07:43 2020

@author: Rohit
"""

import turtle                    # import turtle library
import time
import sys

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("Path Finder")
wn.setup(1300,700)

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
        #red.goto(child.position)
        #red.stamp()

def astarRoute(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while (x, y) != (end_x, end_y):
        x, y =track.pop()
        yellow.goto((x, y))
        yellow.stamp()

maze = Maze()
red = Red()
green = Green()
yellow = Yellow()

walls = []
path = []
track = []

maze_outline(grid1)
start_time = time.time()
astar(start_x,start_y,end_x,end_y)
print((time.time() - start_time))
astarRoute(start_x, start_y)
wn.exitonclick()