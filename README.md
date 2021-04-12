# Maze-Solver

Helloo!
This is a small project that helps you create square mazes and solve them instantly. You can get these mazes solved at the press of a button. 
Please ensure that the maze you create follows the following rules :

## Rules
1. Your maze's first row should have the start point. 
2. Your maze's last row should have the end point. 
3. The first row, first column, last row and last column of your maze should be the border.
Thus all 4 of these should have only walls and no paths (except for the cells of start and end points)
4. The current program can only solve simple mazes i.e. mazes that have only 1 solution, and do not have 
any loops i.e. circular paths. 

## One Time Setup 
This program works on pygame and python. Follow the steps to use it:
1. Download the Maze.py file from GitHub onto your Desktop
2. If you do not have python installed, download and install python 3
3. Use the command "pip install pygame" in your terminal


## Usage
1. Run the program from your command prompt using "python Maze.py"
2. Enter the number of rows in your maze 
3. The pygame window will now pop up. 
4. Click on the cells that you want to turn into walls. 
Walls are shown as black, and possible paths are shown as white cells.
5. In case you want to change a wall to a path, you can click on the same cell again. 
6. Once you have designed your maze, be sure to check it has no circular paths at all. 
7. Press the teal button under the maze to solve it. 
The solution will be shown in Blue in the same maze. 

## Important 
1. In case your maze has loops or circular paths, the program will not work. 
You will get a recursion depth limit exceeded in your command prompt and the pygame window will close.

