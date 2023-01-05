import pygame
import sys
import math
from message_box import show_dialog

# Set up pygame
pygame.init()

# Constants
WIDTH = 1000
HEIGHT = 1000
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dijkstra's Algorithm Visualization")

# Set up the grid
grid = []
for i in range(WIDTH // CELL_SIZE):
    grid.append([])
    for j in range(HEIGHT // CELL_SIZE):
        grid[i].append(0)

# Set up the blocks
blocks = []

# Set up the start and end nodes
start = None
end = None

# Set up the open and closed sets
open_set = []
closed_set = []

# Set up the came_from dictionary
came_from = {}

# Set up the g_score and f_score dictionaries
g_score = {}
f_score = {}

# Set up the diagonal movement cost
diagonal_cost = math.sqrt(2)

# Set up the cost of moving horizontally or vertically
horizontal_vertical_cost = 1

# Flag to check if a path is found
path_found = False

# Flag to check for mouse held down
mouse_held_down = False

def display_message(message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(text, text_rect)
        pygame.display.flip()

# Set up the heuristic function
def heuristic(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Set up the function to retrieve the lowest f_score
def get_lowest_f_score(open_set, f_score):
    lowest = float("inf")
    lowest_node = None
    for node in open_set:
        if node in f_score and f_score[node] < lowest:
            lowest = f_score[node]
            lowest_node = node
    return lowest_node

# Set up the function to reconstruct the path
def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path

# Set up the function to draw the grid
def draw_grid():
    for i in range(HEIGHT // CELL_SIZE):
        for j in range(WIDTH // CELL_SIZE):
            color = (128, 128, 128)
            if grid[i][j] == 1:
                color = BLACK
            elif grid[i][j] == 2:
                color = RED
            elif grid[i][j] == 3:
                color = GREEN
            elif grid[i][j] == 4:
                color = BLUE
            elif grid[i][j] == 5:
                color = YELLOW
            # Draw the cells in light grey
            pygame.draw.rect(screen, color, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)


def reset_grid(grid, open_set, closed_set, came_from, g_score, f_score):
    new_grid = []
    for i in range(WIDTH // CELL_SIZE):
        new_grid.append([])
        for j in range(HEIGHT // CELL_SIZE):
            new_grid[i].append(0)
    return new_grid, [], [], {}, {}, {}

# Set up the function to add blocks
def add_block(pos):
    i = pos[0] // CELL_SIZE
    j = pos[1] // CELL_SIZE
    if i < 0 or i >= HEIGHT or j < 0 or j >= WIDTH:
        return
    if grid[i][j] == 0:
        blocks.append((i, j))
        grid[i][j] = 1
        

# Set up the function to remove blocks
def remove_block(pos):
    i = pos[0] // CELL_SIZE
    j = pos[1] // CELL_SIZE
    if grid[i][j] == 1:
        blocks.remove((i, j))
        grid[i][j] = 0

# Set up the function to set the start node
def set_start(pos):
    global start
    i = pos[0] // CELL_SIZE
    j = pos[1] // CELL_SIZE
    if grid[i][j] == 0:
        if start != None:
            grid[start[0]][start[1]] = 0
        start = (i, j)
        grid[i][j] = 2

# Set up the function to set the end node
def set_end(pos):
    global end
    i = pos[0] // CELL_SIZE
    j = pos[1] // CELL_SIZE
    if grid[i][j] == 0:
        if end != None:
            grid[end[0]][end[1]] = 0
        end = (i, j)
        grid[i][j] = 3

# Set up the function to get the neighbors of a node
def get_neighbors(node):
    i, j = node
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, j))
    if i < HEIGHT // CELL_SIZE - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < WIDTH // CELL_SIZE - 1:
        neighbors.append((i, j + 1))
    if i > 0 and j > 0:
        neighbors.append((i - 1, j - 1))
    if i < HEIGHT // CELL_SIZE - 1 and j < WIDTH // CELL_SIZE - 1:
        neighbors.append((i + 1, j + 1))
    if i > 0 and j <  WIDTH // CELL_SIZE - 1:
        neighbors.append((i - 1, j + 1))
    if i < HEIGHT // CELL_SIZE - 1 and j > 0:
        neighbors.append((i + 1, j - 1))

    # exclude neighbors that are blocks
    neighbors = [neighbor for neighbor in neighbors if grid[neighbor[0]][neighbor[1]] != 1]

    return neighbors

# Set up the main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False
        if mouse_held_down:
            pos = pygame.mouse.get_pos()
            if pos[0]:
                add_block(pos)
            elif pos[1]:
                remove_block(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # set start node
                pos = pygame.mouse.get_pos()
                set_start(pos)
            elif event.key == pygame.K_e:
                # set end node
                pos = pygame.mouse.get_pos()
                set_end(pos)
            elif event.key == pygame.K_r:
                # clear board
                grid, open_set, closed_set, came_from, g_score, f_score = reset_grid(grid, open_set, closed_set, came_from, g_score, f_score)
                start= None
                end = None
            elif event.key == pygame.K_SPACE:
                if start != None and end != None:
                    # Initialize the open and closed sets, as well as the g_score and f_score dictionaries
                    open_set.append(start)
                    closed_set.clear()
                    g_score.clear()
                    f_score.clear()
                    g_score[start] = 0
                    f_score[start] = g_score[start] + heuristic(start, end)


                    open_set = [start]
                    g_score[start] = 0
                    f_score[start] = heuristic(start, end)

                    while len(open_set) > 0:
                        current = get_lowest_f_score(open_set, f_score)
                        if current == end:
                            path = reconstruct_path(came_from, end)
                            for node in path:
                                grid[node[0]][node[1]] = 5
                            path_found = True
                            break

                        open_set.remove(current)
                        closed_set.append(current)
                        grid[current[0]][current[1]] = 4

                        neighbors = get_neighbors(current)
                        for neighbor in neighbors:
                            if neighbor in closed_set:
                                continue
                            tentative_g_score = g_score[current] + horizontal_vertical_cost
                            if neighbor in blocks:
                                tentative_g_score += 10
                            if neighbor in open_set:
                                if tentative_g_score < g_score[neighbor]:
                                    g_score[neighbor] = tentative_g_score
                                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                                    came_from[neighbor] = current
                            else:
                                g_score[neighbor] = tentative_g_score
                                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, end)
                                came_from[neighbor] = current
                                open_set.append(neighbor)
                        draw_grid()
                        pygame.display.update()
                    
                    if not path_found:
                        result = show_dialog(screen, "No path found")
                        if result == "restart":
                            # Restart the program
                            grid, open_set, closed_set, came_from, g_score, f_score = reset_grid(grid, open_set, closed_set, came_from, g_score, f_score)
                            start= None
                            end = None
                        elif result == "quit":
                            # Quit the program
                            pygame.quit()
                            sys.exit()

    draw_grid()
    pygame.display.update()

pygame.quit()
sys.exit()
