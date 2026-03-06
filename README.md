# RL Environment Games - Open Day 2026
**Computer Science and Automation (CSA), IISc Bengaluru**

Welcome to the Reinforcement Learning (RL) interactive showcase! This repository contains the code and demonstrations used for the CSA Open Day 2026. It allows users to interact with the exact classic Atari environments used to train Deep Reinforcement Learning agents, challenge a State-of-the-Art (SOTA) AI in a 1v1 match, and view the visual progression of an AI learning to play from scratch.

## 📂 Repository Structure

```text
OpenDay26_CSA/
├── EnvCodes/                  # Interactive, human-playable Atari scripts
│   ├── at_breakout.py         # Play Breakout (Controls: A/D, Space)
│   ├── at_freeway.py          # Play Freeway (Controls: W/S)
│   ├── at_pacman.py           # Play Ms. Pacman (Controls: W/A/S/D)
│   ├── at_seaquest.py         # Play Seaquest (Controls: W/A/S/D, Space)
│   ├── at_spaceinvaders.py    # Play Space Invaders (Controls: A/D, Space)
│   ├── README.md              # Folder-specific notes
│   └── environment.yml        # Conda environment dependencies
├── SlimeVolley/               # 🤖 Man vs. Machine Arena
│   └── play_slime_lev1.py          # Play 1v1 Volleyball against a SOTA PPO agent
│   └── play_slime_lev2.py          # Play 1v1 Volleyball against a SOTA PPO agent
└── Video_Demonstrations/      # 🎞️ Generated Training Progression Videos
    └── Breakout_Comparison_3col.mp4 
```

---

## Setup & Installation

We recommend using [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda to manage the dependencies.

### 1. Standard Atari Setup
To install the dependencies required for the playable Atari games and video rendering:
```bash
# Navigate to the EnvCodes directory
cd EnvCodes

# Create the environment from the provided YAML file
conda env create -f environment.yml

# Activate the environment
conda activate od
```

### 2. SlimeVolley (Human vs AI) Setup
SlimeVolley requires an older version of the `gym` library. It is highly recommended to run this in a separate, lightweight environment:
```bash
conda create -n slime_env python=3.9
conda activate slime_env

# Install legacy build tools to prevent setup errors
pip install setuptools==65.5.0 wheel==0.38.4

# Install the environment and UI dependencies
pip install gym==0.19.0 slimevolleygym pyglet==1.5.27
```

---


## 📹 Video Demonstrations

The `/Video_Demonstrations` folder contains compiled, multi-column progression videos (rendered using MoviePy and Sample Factory). These videos demonstrate the learning curve of an RL agent over millions of steps.

**Progression Stages Shown:**
1. **Before Training (Untrained):** The agent takes completely random actions.
2. **Early Training:** The agent begins to grasp the basic reward structure (e.g., hitting the ball, moving forward).
3. **Later Training (Fully Trained):** The agent exhibits superhuman reflexes and exploits complex game mechanics (e.g., tunneling in Breakout).

---
*Indian Institute of Science (IISc) - CSA Open Day 2026.*
