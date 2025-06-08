# KEYNAV THE GAME
## Description

Tests your mouse emulator skills and solution!

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
    - [-] **distribute on github**
   - [ ] write propper documentation
- [ ] PHASE II
    - [ ] Custom game settings
        - [ ] button size
        - [ ] Possible button positions by "n" key presses for a 2x2 grid
    - [ ] full screen keybing
    - [ ] better score label
        - [ ] Click per seconds
        - [ ] key presses total
        - [ ] clicks
        - [ ] mean values
    - [ ] deploy
- [ ] PHASE III
    - [ ] Gamify with basic levels
    - [ ] "Choose level" widget
        - [ ] Level 1 - 1 key press away
        - [ ] Level 2 - 2 key presses away - main axes only
        - [ ] Level 3 - 1 or 2 key presses away - main axes only
        - [ ] Level 4 - 2 key presses away - anywhere
        - [ ] Level 5 - 1 or 2 ley presses away - anywhere
- [ ] PHAVE IV
    - [ ] Dual monitor capability
    - [ ] deploy

## DEV NOTES

### Suggested project directory

keynav-the-game/
├── .github/                # GitHub-specific configs (e.g., workflows, issue templates)
│   └── workflows/
│       └── python.yml      # (optional) CI/CD via GitHub Actions
├── src/                    # Python source code
│   └── keynav_game/        # Your actual package or module
│       ├── __init__.py
│       ├── main.py         # Entry point
│       └── gui.py          # GUI logic
├── dist/                   # Built/packaged binaries (gitignored)
│   ├── windows/            # Windows executable(s)
│   └── linux/              # Linux binary or AppImage
├── assets/                 # Icons, images, sound effects, etc.
├── tests/                  # Unit or integration tests
│   └── test_main.py
├── .gitignore              # Exclude dist/, __pycache__, etc.
├── README.md               # Project description & usage
├── LICENSE                 # An OSI-approved license (e.g., MIT)
├── pyproject.toml          # Modern packaging metadata (PEP 621 / poetry / hatch etc.)
├── requirements.txt        # (optional) direct dependencies list
├── setup.py                # (optional legacy) for pip install
├── build.py                # (optional) script to automate builds for Linux/Windows
└── Makefile                # (optional) CLI tasks (build, test, clean, etc.)

