import gymnasium as gym
from gymnasium.utils.play import play
import pygame

keys = {
    # Single key presses
    (pygame.K_SPACE,): 1,         # Spacebar: Shoot
    (pygame.K_RIGHT,): 2,         # Right Arrow: Move Right
    (pygame.K_LEFT,): 3,         # Left Arrow: Move Left
    
    (pygame.K_RIGHT, pygame.K_SPACE): 4,  # Right Arrow + Space: Move Right and Shoot
    (pygame.K_SPACE, pygame.K_RIGHT): 4,  
    (pygame.K_LEFT, pygame.K_SPACE): 5,  # Left Arrow + Space: Move Left and Shoot
    (pygame.K_SPACE, pygame.K_LEFT): 5,
}

if __name__ == "__main__":
    env = gym.make("SpaceInvadersNoFrameskip-v4", render_mode="rgb_array")
    
    print("=================================================")
    print("Space Invaders Controls:")
    print(" - [RIGHT] / [LEFT]: Move Left and Right")
    print(" - [SPACE]: Fire Laser")
    print(" - You CAN move and shoot at the same time!")
    print("=================================================")

    play(env, keys_to_action=keys, fps=30, zoom=4)