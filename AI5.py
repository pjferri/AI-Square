import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

# Create a square
sq = np.full((10,10), 0.0)

# Create a level
level = np.zeros((10,10))
level[0,0] = 1
level[9,9] = 2

# Create an array to keep track of the square's position
pos = np.array([0,0])

# Create a function that will move the square
def move_sq(sq, pos, direction):
    if(direction == 'left'):
        if(pos[1] > 0):
            pos[1] -= 1
    elif(direction == 'right'):
        if(pos[1] < 9):
            pos[1] += 1
    elif(direction == 'up'):
        if(pos[0] > 0):
            pos[0] -= 1
    elif(direction == 'down'):
        if(pos[0] < 9):
            pos[0] += 1
    else:
        return (sq, pos)
    
    # Set the position of the square
    sq[pos[0], pos[1]] = 1.0
    return (sq, pos)

# Create a function that will generate a random move
def random_move():
    moves = ['left', 'right', 'up', 'down']
    move = np.random.choice(moves)
    return move

# Define the colors for the different elements in the maze
level_color = 'Oranges'
square_color = 'coolwarm'

# Create a loop that will keep running until the square reaches the end
while(sq[pos[0], pos[1]] != 2):
    # Generate a random move
    direction = random_move()
    
    # Move the square
    sq, pos = move_sq(sq, pos, direction)
    
    # Display the level and the square
    plt.imshow(level, cmap=level_color)
    plt.imshow(sq, cmap=square_color, alpha=0.75)
    plt.pause(0.0001)