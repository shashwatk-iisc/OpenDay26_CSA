# Atari Gymnasium Setup

This project sets up a Python environment to **play Atari games using Gymnasium**.

Supported games in this project:

* Breakout
* Freeway
* MsPacman
* Seaquest
* SpaceInvaders
* JamesBond

These environments run through the Arcade Learning Environment (ALE).

---

# Environment Setup

Create the conda environment:

```bash
conda env create -f environment.yml
conda activate gym-atari-play
```

---

# Install Atari ROMs

After activating the environment, install the Atari ROMs:

```bash
AutoROM --accept-license
```

---

# Run the Game

Example run:

```bash
python at_breakout.py
```

---

# Example Environment IDs

```python
ALE/Breakout-v5
ALE/Freeway-v5
ALE/MsPacman-v5
ALE/Seaquest-v5
ALE/SpaceInvaders-v5
ALE/Jamesbond-v5
```

---

# Controls (Example)

| Key   | Action       |
| ----- | ------------ |
| SPACE | Fire / Start |
| LEFT  | Move left    |
| RIGHT | Move right   |

```
```
