# KEYNAV THE GAME
## Description

**Tests your mouse emulator skills and solution!**

This is mainly a personal *"hello world"* project for me. Written in python, it was mainly made to familiarize myself with the [kivy](https://kivy.org) GUI framework.

Nonetheless this game is intended to practice your keyboard navigation skills. It was based with the [jordansissel/keynav](https://github.com/jordansissel/keynav) tool in mind.

For now it is mostly only a proof of concept, but I might work on it a little more in the future.

## Installation

### Linux

Simply paste this command in your terminal:

```bash
sudo curl -L https://github.com/placerte/keynav-the-game/releases/download/v0.1.0/keynav-game-0.1.1-linux-x86_64 -o /usr/local/bin/keynav-game
sudo chmod +x /usr/local/bin/keynav-game
```


## Development Roadmap

- [-] **PHASE I**
    - [x] Choose cross platform GUI framework
    - [x] Install cross platform GUI framework
    - [x] ~Setup deployment project structure~
    - [x] ~Basic fullscreen UI - single monitor~
    - [x] ~Bump out out bounds button~
    - [x] ~Put game logic into game_logic.py~
    - [x] ~Random button position~
    - [x] ~basic label click count~
    - [ ] compile for windows
    - [x] ~compile for linux~
    - [x] ~distribute on github~
   - [x] ~write proper documentation~
- [ ] PHASE II
    - [ ] Custom game settings
        - [ ] button size
        - [ ] Possible button positions by "n" key presses for a 2x2 grid
    - [x] ~full screen keybing~
    - [ ] better score label
        - [x] ~Click per seconds~
        - [ ] key presses total
        - [x] ~clicks~
        - [x] ~mean values~
    - [ ] deploy
- [ ] PHASE III
    - [ ] Gamify with basic levels
    - [ ] "Choose level" widget
        - [ ] Level 1 - 1 key press away
        - [ ] Level 2 - 2 key presses away - main axes only
        - [ ] Level 3 - 1 or 2 key presses away - main axes only
        - [ ] Level 4 - 2 key presses away - anywhere
        - [ ] Level 5 - 1 or 2 ley presses away - anywhere
- [ ] PHASE IV
    - [ ] Dual monitor capability
    - [ ] deploy
