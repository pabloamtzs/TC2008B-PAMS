import pygame
import sys

pygame.init()

# Set up the display
screen_width = 500
screen_height = 460
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labyrinth Maze Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
orange = (254,235,201)
orange2 = (252,169,133)
purple = (165,137,193)

# Font
font = pygame.font.Font(None, 36)

# Win condition
win_condition_met = False  

# Clock to control frame rate
clock = pygame.time.Clock()

# Define the maze
maze = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X00000X0000000000000X000X",
    "X0X0XXX0XXXXXXXXX0XXX0X0X",
    "X0X0X000X0000000X000X0X0X",
    "X0X0X0XXX0XXX0XXXXX0X0X0X",
    "X0X000X000X000X000X000X0X",
    "X0XXXXXXXXX0XXX0X0XXXXX0X",
    "X0X000000000X000X000X000X",
    "X0X0XXX0X0XXX0XXXXX0X0XXX",
    "X0X0X0X0X0X000X000X0X000X",
    "X0X0X0X0X0X0XXX0XXX0XXX0X",
    "SEX000X0X0X00000X00000X0X",
    "X0XXXXX0XXXXX0XXX0XXX0XOX",
    "X00000X000X000X000X000X0E",
    "XXXXX0X0X0X0XXX0XXX0XXXXX",
    "X000X0X0X0X0X000X0X0X000X",
    "X0X0X0XXX0X0X0XXX0X0X0X0X",
    "X0X0X000X0X0X000X0X0X0X0X",
    "X0X0XXX0X0X0XXXXX0X000X0X",
    "X0X000X0X0X0000000X0XXX0X",
    "X0XXXXX0X0XXXXXXXXX0X0X0X",
    "X0000000X0000000000000X0X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Player settings
cell_size = 20
player_x = 0
player_y = 220

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if maze[int((player_y - cell_size) / cell_size)][int(player_x / cell_size)] != "X":
                    player_y -= cell_size
            elif event.key == pygame.K_DOWN:
                if maze[int((player_y + cell_size) / cell_size)][int(player_x / cell_size)] != "X":
                    player_y += cell_size
            elif event.key == pygame.K_LEFT:
                if maze[int(player_y / cell_size)][int((player_x - cell_size) / cell_size)] != "X":
                    player_x -= cell_size
            elif event.key == pygame.K_RIGHT:
                if maze[int(player_y / cell_size)][int((player_x + cell_size) / cell_size)] != "X":
                    player_x += cell_size

            # Check for win condition
            if maze[int(player_y / cell_size)][int(player_x / cell_size)] == "E":
                win_condition_met = True

    # Clear the screen
    if win_condition_met:
        screen.fill(orange2)
        win_message = font.render("Ganaste!", True, white)
        screen.blit(win_message, (screen_width // 2 - win_message.get_width() // 2, screen_height // 2 - win_message.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(2500)  # Display the message for 2 seconds
        pygame.quit()
        sys.exit()
    else:
        screen.fill(orange)

    # Draw the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "X":
                pygame.draw.rect(screen, orange2, (x * cell_size, y * cell_size, cell_size, cell_size))
            elif cell == "S":
                pygame.draw.circle(screen, (0, 255, 0), (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), 5)
            elif cell == "E":
                pygame.draw.circle(screen, (255, 0, 0), (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), 5)

    # Draw the player
    pygame.draw.circle(screen, purple, (player_x + cell_size // 2, player_y + cell_size // 2), 10)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(30)
