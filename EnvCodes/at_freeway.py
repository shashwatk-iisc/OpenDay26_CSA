import gymnasium as gym
from gymnasium.utils.play import play
import pygame

keys = {
    (pygame.K_UP,): 1,  # W: Move paddle up
    (pygame.K_DOWN,): 2,  # S: Move paddle down
}
if __name__ == "__main__":
    env_id = "FreewayNoFrameskip-v4"
    
    env = gym.make(env_id, render_mode="rgb_array")
    print("Actions the game expects:", env.unwrapped.get_action_meanings())
    print("=================================================")
    print(f"Starting {env_id}")
    print("=================================================")
    print("Controls:")
    print(" - [UP]: Run forward across the highway")
    print(" - [DOWN]: Retreat!")
    print("=================================================")

    play(env, keys_to_action=keys, fps=30, zoom=4)