import gym
import slimevolleygym
import time
from pyglet.window import key

env = gym.make("SlimeVolley-v0")

# SlimeVolley actions are arrays of 3 values: [Forward, Backward, Jump]
# Since you are on the Right side:
# Forward = Move Left (towards the net)
# Backward = Move Right (away from the net)
human_action = [0, 0, 0]

env.reset()
env.render()

@env.viewer.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        human_action[0] = 1  # Forward (towards net)
    elif symbol == key.RIGHT:
        human_action[1] = 1  # Backward (away from net)
    elif symbol == key.UP:
        human_action[2] = 1  # Jump

@env.viewer.window.event
def on_key_release(symbol, modifiers):
    if symbol == key.LEFT:
        human_action[0] = 0
    elif symbol == key.RIGHT:
        human_action[1] = 0
    elif symbol == key.UP:
        human_action[2] = 0

if __name__ == "__main__":
    print("=================================================")
    print("Human vs. AI: Slime Volleyball!")
    print("=================================================")
    print(" Controls (You are the Right Slime):")
    print(" - [LEFT] / [RIGHT]: Move")
    print(" - [UP]: Jump")
    print(" First to 5 points wins. Good luck!")
    print("=================================================")

    obs = env.reset()
    done = False
    human_score = 0
    ai_score = 0

    while not done:
        env.render()

        obs, reward, done, info = env.step(human_action)
        
        # Reward is +1 if you score, -1 if the AI scores
        if reward > 0:
            human_score += 1
            print(f"SCORE! Human: {human_score} | AI: {ai_score}")
        elif reward < 0:
            ai_score += 1
            print(f"Oof... Human: {human_score} | AI: {ai_score}")
            
        # Lock the frame rate to ~50 FPS so the game is playable
        time.sleep(0.02)

    print("\n=================================================")
    if human_score > ai_score:
        print("🎉 YOU BEAT THE MACHINE! 🎉")
    else:
        print("🤖 THE MACHINE WINS! 🤖")
    print("=================================================")
    
    env.close()