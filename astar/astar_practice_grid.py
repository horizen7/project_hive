import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import heapq

#-------FUNCTION TO CALCULATE THE HEURISTIC FROM THE GOAL TO A NODE USING MANHATTEN DISTANCE---------
# def heuristic(node, goal):

#     #I think this just draws a line from the reference node to the goal, and that the "distance" (I think actual distance is sqrt'ed)
#     return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

import math

def heuristic(node, goal):
    return math.sqrt((node[0] - goal[0])**2 + (node[1] - goal[1])**2)

#-------FUNCTION TO GET VALID NEIGBORS GIVEN SOME NODE---------
def get_neighbors(node, walls, width, height):
    x, y = node
    neighbors = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in walls:
            neighbors.append((nx, ny))

    #return a list of valid nodes given some reference node
    return neighbors


#------MODIFIED A START WHERE GRAPH IS 2D MATRIX OF NODES----------
def a_star_grid(start, goal, walls, width, height):
    open_set = [(heuristic(start, goal), start)]
    g_costs = {start: 0}
    came_from = {}
    

    #A stack entry can get popped out but if it doesn't satisfy if conditions it amasses to nothing 
    while open_set:
        current_f, current_node = heapq.heappop(open_set)
        
        if current_node == goal:
            # Reconstruct path
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]
            
        for neighbor in get_neighbors(current_node, walls, width, height):
            # The cost to move one grid space is always 1; the g cost of any individual node is not required to change after set
            # neighbor is some tupled coordinate
            tentative_g_cost = g_costs[current_node] + 1
            
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]: #chooses which path to take 
                came_from[neighbor] = current_node #from example of starting node like saying "came from neighbor, the starting node (S -> neighbor)"
                g_costs[neighbor] = tentative_g_cost
                
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_cost, neighbor))

    return None # No path found

# --- 2. SET UP THE WORLD ---
WIDTH, HEIGHT = 10, 10
START = (0, 0)
GOAL = (8, 9)

# Build a small maze/obstacle course
WALLS = {(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 2), 
         (6, 6), (7, 6), (8, 6), (8, 7), (8, 8), (6, 7), (6, 8)}

# Run the algorithm
PATH = a_star_grid(START, GOAL, WALLS, WIDTH, HEIGHT)





# --- 3. VISUALIZE WITH MATPLOTLIB ---
# Create an empty grid filled with 0s (0 = empty space)
grid = np.zeros((HEIGHT, WIDTH))

# Paint the walls on the grid (1 = Wall)
for wx, wy in WALLS:
    grid[wy, wx] = 1 # Note: arrays are mapped as [row (y), column (x)]

# Paint the path (2 = Path)
if PATH:
    for px, py in PATH:
        grid[py, px] = 2

# Paint Start (3) and Goal (4)
grid[START[1], START[0]] = 3
grid[GOAL[1], GOAL[0]] = 4

# Map the numbers 0, 1, 2, 3, 4 to actual colors
cmap = mcolors.ListedColormap(['white', 'black', 'dodgerblue', 'limegreen', 'red'])

# Setup the window
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(grid, cmap=cmap)

# Add gridlines so we can actually see the squares
ax.set_xticks(np.arange(-0.5, WIDTH, 1), minor=True)
ax.set_yticks(np.arange(-0.5, HEIGHT, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=1)
ax.tick_params(which='minor', size=0)

plt.title("A* Pathfinding Visualization")
plt.savefig('astar_result.png', bbox_inches='tight')
print("Image saved as astar_result.png!")