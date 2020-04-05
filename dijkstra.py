# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:13:24 2020

@author: Arzoo
"""

import turtle                    # import turtle library
import sys
from math import inf as infinity

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.title("A Djikstra Maze Solving Program")
wn.setup(1300,700)                  # setup the dimensions of the working window


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
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


# grid = [
# "+++++++++++++++",
# "+s+       + +e+",
# "+ +++++ +++ + +",
# "+ + +       + +",
# "+ +   +++ + + +",
# "+ + + +   + + +",
# "+   + +   + + +",
# "+++++ +   + + +",
# "+     +   +   +",
# "+++++++++++++++",
# ]

# grid = [
# "+++++++++",
# "+ ++s++++",
# "+ ++ ++++",
# "+ ++ ++++",
# "+    ++++",
# "++++ ++++",
# "++++ ++++",
# "+      e+",
# "+++++++++",
# ]

# grid = [
# "+++++++++++++++",
# "+             +",
# "+             +",
# "+             +",
# "+     e       +",
# "+             +",
# "+             +",
# "+             +",
# "+ s           +",
# "+++++++++++++++",
# ]
grid = [
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
"+      ++ +++++++e+++     ++          ++    +++++++",
"+++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]


def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y ,start, end, nodes    # set up global variables for start and end locations
    
    nodes = [[None for x in range(len(grid[0]))] for y in range(len(grid))]
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list
                nodes[y][x] = None
                
            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list
                nodes[y][x] = Node(x, y)
            
            if character == "e":
                green.color("purple")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")
                nodes[y][x] = Node(x, y)
                end = (x, y)

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)
                nodes[y][x] = Node(x, y)
                start = (x, y)

class Graph:
    def __init__(self, graph, start, end):
        self.graph = graph
        self.start_node = graph[start[1]][start[0]]
        self.end_node = graph[end[1]][end[0]]

    def getNodes(self):
        return [node for row in self.graph for node in row]

    def getNeighbors(self, node):
        neighbors = []
        if (node.y != 0):
            neighbors.append(self.graph[node.y - 1][node.x])
        if (node.y != len(self.graph) - 1):
            neighbors.append(self.graph[node.y + 1][node.x])
        if (node.x != 0):
            neighbors.append(self.graph[node.y][node.x - 1])
        if (node.x != len(self.graph[node.y]) - 1):
            neighbors.append(self.graph[node.y][node.x + 1])
        return neighbors


class Node:
    tentative_distance = None
    visited = False

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return 1

def endProgram():
    wn.exitonclick()
    sys.exit()
def dijkstra(graph):
    start_node = graph.start_node
    end_node = graph.end_node

    unvisited = set(graph.getNodes())


    start_node.temp_dist = 0
    for node in unvisited:
        if node and node is not start_node:
            node.temp_dist = infinity

    current_node = start_node

    while not end_node.visited:

        for neighbor in graph.getNeighbors(current_node):
            if not neighbor or neighbor.visited:
                continue
            new_temp_dist = current_node.temp_dist + current_node.distance_to(neighbor)
            if neighbor.temp_dist > new_temp_dist:
                neighbor.temp_dist = new_temp_dist

        current_node.visited = True
            
        green.goto((-588 + (current_node.x * 24)), (288 - (current_node.y * 24)))
        unvisited.remove(current_node)

        shortest_temp_dist = infinity
        for node in unvisited:
            if node and node.temp_dist < shortest_temp_dist:
                shortest_temp_dist = node.temp_dist
                current_node = node

    return end_node.temp_dist

def djikstraBackRoute(end_dist):
        start_node = graph.graph[start[1]][start[0]]
        end_node = graph.graph[end[1]][end[0]]

        nodes = graph.getNodes()

        for node in nodes:
            if node:
               node.visited = False

        current_node = end_node
        shortest_temp_dist = end_dist
        # backtacking yellow path from end node to start node
        while current_node is not start_node:
        
          neighbors = graph.getNeighbors(current_node)
          for neighbor in neighbors:
             if not neighbor or neighbor.visited:
                continue
             if neighbor.temp_dist < shortest_temp_dist:
                shortest_temp_dist = neighbor.temp_dist
                neighbor.visited = True
                current_node = neighbor
          yellow.goto((-588 + (current_node.x * 24)), (288 - (current_node.y * 24)))
          yellow.stamp()
        
# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []

# main program starts here ####
setup_maze(grid)

graph = Graph(nodes, start, end)

end_dist = dijkstra(graph)

djikstraBackRoute(end_dist)

wn.exitonclick()
