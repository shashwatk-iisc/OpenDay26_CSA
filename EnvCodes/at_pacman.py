import gymnasium as gym
from gymnasium.utils.play import play
import pygame

keys = {
    (pygame.K_UP,): 1,  # W: Move Up
    (pygame.K_RIGHT,): 2,  # D: Move Right
    (pygame.K_LEFT,): 3,  # A: Move Left
    (pygame.K_DOWN,): 4,  # S: Move Down
}

if __name__ == "__main__":
    env = gym.make("MsPacmanNoFrameskip-v4", render_mode="rgb_array")
    
    print("=================================================")
    print("Ms. Pacman Controls:")
    print(" - [↑]: Move Up")
    print(" - [↓]: Move Down")
    print(" - [←]: Move Left")
    print(" - [→]: Move Right")
    print(" Note: The game auto-starts, just start moving!")
    print("=================================================")

    # Launch the  window
    play(env, keys_to_action=keys, fps=30, zoom=4)