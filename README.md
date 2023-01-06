# A-Path-Finding-Visualization
A* is a popular pathfinding algorithm that is used to find the shortest path between two points on a grid. It combines the use of a heuristic function with the cost of movement to efficiently search through the grid and find the optimal path. A* is commonly used in computer science and game development to allow objects to navigate around obstacles and find the most efficient path to their destination. Working on this project has allowed me to further my understanding of algorithms and their practical applications, as well as work on my skills in GUI and front end development.

![](pathfindingGIF.gif)

## Overview
This program allows the user to create blocks on a grid by clicking and dragging the mouse, which will be used to represent walls or obstacles. The user can then select a start node by clicking on a cell and then selecting an end node by clicking on a different cell. The program will then use the A* algorithm to find the shortest path between the start and end nodes, represented by a yellow line. If no path is found, a message will be displayed to the user. The program also has a "Restart" button that allows the user to clear the grid and start over, as well as a "Quit" button to exit the program. The cells on the grid will change color to indicate their status during the A* algorithm: black cells are walls or obstacles, red represents the start cell, green represents the end cell, and yellow cells are part of the final path.

## User Actions
1. `Left-Click-Drag` will create 'walls' or 'obstacles'
2. `S-Key` on a cell will make a cell red (start cell)
3. `E-Key` on a cell will make a cell green (end cell)
4. `R-Key` will reset the grid
5. `Spacebar` will begin the A* pathfinding algorithm if a start and end cell are selected


## Instructions for Running the Application
1. Make sure you have Python 3 installed on your machine. You can check if you have Python installed by opening a terminal and typing "python3 --version". If you do not have Python installed, you can download it from the official Python website (https://www.python.org/downloads/).

2. Next, you will need to install pygame. You can do this by typing "pip3 install pygame" in your terminal.

3. Once you have Python and pygame installed, download the files from the github repository onto your machine.

4. Navigate to the directory where the files are saved using your terminal.

5. Run the program by typing "python3 path_finding.py" in your terminal. The program should now start and you can use it to visualize Dijkstra's algorithm.
