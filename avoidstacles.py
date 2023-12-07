import random
import pygame
import tkinter as tk

# initialize pygame
pygame.init()

# set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Avoid Obstacles")

# set up the game objects
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10

obstacle_width = 50
obstacle_height = 50
obstacle_speed = 5
obstacles = []

# set up the game font
font = pygame.font.Font(None, 30)

# set up the tkinter window for selecting the game mode
def set_easy_mode():
    global obstacle_speed
    obstacle_speed = 3
    root.destroy()

def set_medium_mode():
    global obstacle_speed
    obstacle_speed = 5
    root.destroy()

def set_hard_mode():
    global obstacle_speed
    obstacle_speed = 10
    root.destroy()

root = tk.Tk()
root.title("Select Game Mode")
easy_button = tk.Button(root, text="Easy", command=set_easy_mode)
easy_button.pack()
medium_button = tk.Button(root, text="Medium", command=set_medium_mode)
medium_button.pack()
hard_button = tk.Button(root, text="Hard", command=set_hard_mode)
hard_button.pack()
root.mainloop()

# game loop
score = 0
clock = pygame.time.Clock()
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    elif keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += 5

    # move the obstacles and add new ones
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
    if len(obstacles) == 0 or obstacles[-1][1] > 50:
        x = random.randint(0, window_width - obstacle_width)
        obstacles.append([x, -obstacle_height])
    if obstacles[0][1] > window_height:
        obstacles.pop(0)

    # check for collisions
    for obstacle in obstacles:
        if player_x < obstacle[0] + obstacle_width and player_x + player_width > obstacle[0] and player_y < obstacle[1] + obstacle_height and player_y + player_height > obstacle[1]:
            running = False
    
    # update the score
    score += 1

    # draw the game
    window.fill((0, 0, 0))
    for obstacle in obstacles:
        pygame.draw.rect(window, (255, 0, 0), (obstacle[1], obstacle[0], obstacle_width, obstacle_height))
    pygame.draw.rect(window, (0, 0, 255), (player_x, player_y, player_width, player_height))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 20))

    # update the display
    pygame.display.update()

    # limit the frame rate
    clock.tick(60)

# clean up pygame
pygame.quit()
print("Score =",score)