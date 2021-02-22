# Multiple balls bouncing around the screen at the same time

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25

# Class to keep track of a ball's location and vector
class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

# Function to make a new, random ball
def make_ball():
    ball = Ball()

    # Starting position of the ball. Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    # Speed and direction of the ball
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    return ball

# Main program
def main():
    # Initialize all imported pygame modules
    pygame.init()

    # Set the width and height of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    # Set the screen caption
    pygame.display.set_caption("Bouncing Multiple Balls")

    # Loop until the user clicks the close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []
    
    ball = make_ball()
    ball_list.append(ball)

    # Main loop
    while not done:
        # Event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Spawn a new ball when space bar is hit
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1

        # Drawing
        # Set the screen background
        screen.fill(BLACK)

        # Draw the ball
        for ball in ball_list:
            pygame.draw.circle(screen, RED, [ball.x, ball.y], BALL_SIZE)

        # Wrap up
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn
        pygame.display.flip()

    # Uninitialize all pygame modules: Close everything down
    pygame.quit()

if __name__ == "__main__":
    main()
