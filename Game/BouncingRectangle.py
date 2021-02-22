# Bounce a rectangle around the screen

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
Blue = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
RECT_SIZE = 50  # One side of square

# Initialize all imported pygame modules
pygame.init()

# Set the width and height of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

# Set the screen caption
pygame.display.set_caption("Bouncing Rectangle")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = random.randrange(-2, 3)
rect_change_y = random.randrange(-2, 3)

# Loop until the user clicks the close button
done = False

# Main loop
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move the rectangle to starting point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the ball if needed
    if rect_x > SCREEN_WIDTH - RECT_SIZE or rect_x < 0:
        rect_change_x *= -1
    if rect_y > SCREEN_HEIGHT - RECT_SIZE or rect_y < 0:
        rect_change_y *= -1

    # Drawing
    # Set the screen background
    screen.fill(BLACK)

    # Draw the rectangle
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, RECT_SIZE, RECT_SIZE])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, RECT_SIZE - 20, RECT_SIZE - 20])

    # Wrap up
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

# Uninitialize all pygame modules: Close everything down
pygame.quit()

