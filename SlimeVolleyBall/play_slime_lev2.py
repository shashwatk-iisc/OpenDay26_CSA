import gym
import slimevolleygym
import time
from pyglet.window import key

from slimevolleygym.mlp import makeSlimePolicyLite

env = gym.make("SlimeVolley-v0")

# Load the GA Self-Play model
ga_model_path = "zoo/ga_sp/ga.json"
print(f"Loading GA (Self-Play) model from {ga_model_path}...")
ai_policy = makeSlimePolicyLite(ga_model_path)

human_action = [0, 0, 0]

env.reset()
env.render()

@env.viewer.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        human_action[0] = 1
    elif symbol == key.RIGHT:
        human_action[1] = 1
    elif symbol == key.UP:
        human_action[2] = 1

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
    print("Human vs. GA Self-Play: Slime Volleyball!")
    print("=================================================")
    print(" Controls (You are the Right Slime):")
    print(" - [LEFT] / [RIGHT]: Move")
    print(" - [UP]: Jump")
    print(" First to 5 points wins. Good luck!")
    print("=================================================")
    obs1 = env.reset()
    obs2 = obs1
    
    done = False
    human_score = 0
    ai_score = 0

    while not done:
        env.render()

        # Get AI action from the GA policy
        ai_action = ai_policy.predict(obs2)

        # Step 
        obs1, reward, done, info = env.step(human_action, ai_action)
        obs2 = info['otherObs'] 

        if reward > 0:
            human_score += 1
            print(f"SCORE! Human: {human_score} | AI: {ai_score}")
        elif reward < 0:
            ai_score += 1
            print(f"Oof... Human: {human_score} | AI: {ai_score}")
            
        time.sleep(0.02)

    print("\n=================================================")
    if human_score > ai_score:
        print("🎉 YOU BEAT THE MACHINE! 🎉")
    else:
        print("🤖 THE MACHINE WINS! 🤖")
    print("=================================================")
    
    env.close()