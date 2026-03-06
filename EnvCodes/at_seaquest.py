import gymnasium as gym
from gymnasium.utils.play import play
import pygame

# Atari Seaquest Action Space (Main actions):
# 0: NOOP (Do nothing)
# 1: FIRE (Shoot torpedo)
# 2: UP (Move Up)
# 3: RIGHT (Move Right)
# 4: LEFT (Move Left)
# 5: DOWN (Move Down)
# 6: UPFIRE (Move Up + Shoot)
# 7: RIGHTFIRE (Move Right + Shoot)
# 8: LEFTFIRE (Move Left + Shoot)
# 9: DOWNFIRE (Move Down + Shoot)

keys = {
    # Single key presses
    (pygame.K_SPACE,): 1,         # Spacebar: Shoot
    (pygame.K_UP,): 2,         # W: Move Up
    (pygame.K_RIGHT,): 3,         # D: Move Right
    (pygame.K_LEFT,): 4,         # A: Move Left
    (pygame.K_DOWN,): 5,         # S: Move Down
    
    # Combined key presses 
    (pygame.K_UP, pygame.K_SPACE): 6,  # W + Space: Move Up and Shoot
    # (pygame.K_SPACE, pygame.K_UP): 6,  
    (pygame.K_RIGHT, pygame.K_SPACE): 7,  # D + Space: Move Right and Shoot
    # (pygame.K_SPACE, pygame.K_RIGHT): 7,
    (pygame.K_LEFT, pygame.K_SPACE): 8,  # A + Space: Move Left and Shoot
    # (pygame.K_SPACE, pygame.K_LEFT): 8,
    (pygame.K_DOWN, pygame.K_SPACE): 9,  # S + Space: Move Down and Shoot
    # (pygame.K_SPACE, pygame.K_DOWN): 9,
}

if __name__ == "__main__":
    env = gym.make("SeaquestNoFrameskip-v4", render_mode="rgb_array")
    
    print("=================================================")
    print("Seaquest Controls:")
    print(" - [UP/DOWN/LEFT/RIGHT]: Move your submarine")
    print(" - [SPACE]: Fire torpedoes")
    print(" - You CAN move and shoot at the same time!")
    print("\n Pro-Tip: Don't forget to surface at the top of the ")
    print(" screen to refill your oxygen bar at the bottom!")
    print("=================================================")

    play(env, keys_to_action=keys, fps=30, zoom=4)