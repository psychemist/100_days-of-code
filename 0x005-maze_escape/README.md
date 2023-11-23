# Reeborg's Maze Solver

Reeborg, our trusty robot friend, has found itself lost in a dark maze with a drained flashlight. It needs your help to find the exit using a strategic approach. The goal is to navigate along the right edge of the maze, turning right whenever possible, moving straight ahead if it can't turn right, and turning left as a last resort.

## Problem Description

Reeborg is in a maze, and you can visualize the maze and help Reeborg solve it on [Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json).  The task is to write a Python program using the provided Reeborg functions to guide Reeborg out of the maze.

## Problem-Solving Approach

To achieve the goal, you will need to use the following functions and conditions:

- `move()`: Move Reeborg one step forward.
- `turn_left()`: Turn Reeborg 90 degrees to the left.
- `front_is_clear()`: Check if the path in front of Reeborg is clear.
- `right_is_clear()`: Check if the path to the right of Reeborg is clear.
- `at_goal()`: Check if Reeborg has reached the exit.

Your program should utilize a while loop and if/elif/else statements to implement the logic of moving along the right edge of the maze.

Simply run the code in the Reeborg environment, and watch as Reeborg successfully navigates its way out of the maze by following the right edge.

Happy coding, and may Reeborg find its way to freedom! 🤖🔍🚀
