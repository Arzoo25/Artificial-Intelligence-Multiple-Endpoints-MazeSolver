# Artificial Intelligence Project
Maze Solver using:  Breadth First Search, Depth First Search, A star, Modified BFS, Modified DFS

The initial approach was to start with a single endpoint and develop all the algorithms and then move on to multiple endpoints.
The purpose of introducing multiple endpoints is to see how efficiently the algorithms will traverse all the points.

PathFinderMain.py is the main file which contains all the algorithms and it can be run as it is to execute each algorithm.

For selection of algorithm: 1- BFS, 2- DFS, 3- A star, 4- Modified BFS, 5- Modified DFS.

For selection  of grid: 1- Single endpoint, 2- Two enpoints, 3- three endpoints.

We have made a generalised algorithm which will work similarly for any number of endpoints.
Based on different scenarios and complexity of the maze, Modified DFS is a good choice.
But if an optimal path is needed irrespective of time and complexity, BFS and A star algorithm can be used.
Modified BFS and Modified DFS performed well in many cases compared to BFS and DFS.
Result.docx file is added with grids used and images of solved maze with all the algorithms along with the time taken to complete it.
