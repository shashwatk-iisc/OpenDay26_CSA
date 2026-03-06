# Slime Volleyball: Human vs AI 🏐

Welcome to Slime Volleyball! This project pits you (a human player) against pre-trained Reinforcement Learning agents. Can you beat the machine?

## The Two Levels of Difficulty

We have structured the AI opponents into two distinct levels. You can play them by running their respective Python scripts.

* **Level 1: The Default AI (Normal Mode) - `play_slime_lev1.py`**
    * **Opponent:** Built-in RNN Baseline Policy.
    * **Description:** This agent was trained using standard self-play back in 2015. It is a great warm-up opponent. It has a static playing style, making it predictable once you figure out its patterns.

* **Level 2: The GA Agent (Boss Mode) - `play_slime_lev2.py`**
    * **Opponent:** Genetic Algorithm (Self-Play) Policy.
    * **Description:** This is the ultimate boss. Instead of training against a static AI, this agent evolved by playing thousands of generations against mutations of itself. It has developed a highly generalized, defensive playstyle that adapts incredibly well to unpredictable human movements. 

## 🛠️ Setup & Installation

This environment relies on older versions of `gym` and `tensorflow`, so **Python 3.7 is strictly required**. We highly recommend using Conda.

### 1. Create the Environment
```bash
conda create -n slimegym python=3.7
conda activate slimegym
```
### 2. Install Core Dependencies

Install the strictly versioned libraries to prevent API-breaking changes:
```
pip install setuptools==65.5.0 wheel
pip install gym==0.19.0 pyglet==1.5.11 numpy==1.19.5 opencv-python
```
### 3. Install SlimeVolleyGym

Clone the repository (if you haven't) and install it in editable mode:
```
git clone [https://github.com/hardmaru/slimevolleygym.git](https://github.com/hardmaru/slimevolleygym.git)
cd slimevolleygym
pip install -e .
```

### 4. Install AI Libraries (Stable Baselines & MPI)

To load the pre-trained neural networks without Protobuf or MPI errors, run:
```
conda install mpi4py
pip install tensorflow==1.15.0 stable-baselines==2.10.0 "protobuf<=3.20.3"
```

# 🚀 How to Play

Make sure your Conda environment is activated, then run either of the levels from the root of the repository:

Play Level 1 (Normal):
```
python play_slime_lev1.py
```

Play Level 2 (Boss):
```
python play_slime_lev2.py
```

# ⌨️ Controls

You control the Right Slime (Yellow).

    Move Left (Towards Net): LEFT ARROW

    Move Right (Away from Net): RIGHT ARROW

    Jump: UP ARROW

First to score 5 points wins the match. Good luck!
