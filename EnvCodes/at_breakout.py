import gymnasium as gym
from gymnasium.utils.play import play
import pygame

# Atari Breakout Action Space:
# 0: NOOP 
# 1: FIRE (Serve the ball / Start)
# 2: RIGHT
# 3: LEFT


key_mapping = {
    (pygame.K_SPACE,): 1,  # Press Spacebar to serve the ball
    (pygame.K_RIGHT,): 2,  # Press Right Arrow to move paddle right
    (pygame.K_LEFT,): 3,   # Press Left Arrow to move paddle left
}

if __name__ == "__main__":
    env_id = "BreakoutNoFrameskip-v4"
    
    env = gym.make(env_id, render_mode="rgb_array")
    
    print("=================================================")
    print(f"Starting {env_id}")
    print("=================================================")
    print("Controls:")
    print(" - [SPACE]: Serve the ball")
    print(" - [LEFT] / [RIGHT]: Move paddle")
    print("=================================================")

    play(env, keys_to_action=key_mapping, fps=30, zoom=4)