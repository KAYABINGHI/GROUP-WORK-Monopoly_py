🎲 MONOPOLY GAME — Python Edition (CLI)

A Python-powered, terminal-based recreation of the classic Monopoly experience. This edition focuses on economic decision-making, turn-based strategy, and an engaging CLI using modern Python tooling. It’s ideal for learning OOP design, state management, testing, and collaborative development—mirroring the structure of the React project while adapting it for Python.

✅ Main Purpose

Simulate economic decision-making: Buy properties, pay rent, upgrade, and manage cash flow.

Engaging multiplayer loop: Players take turns, roll dice, traverse the board, and trigger events.

Teach basic economics: ROI, liquidity, bankruptcy, and asset value via gameplay.

Learning project: Showcases Python app architecture, CLI UX, and testable game logic.

👥 Target Users

Board-game fans who enjoy a strategic CLI experience.

Students/educators exploring economics and algorithms hands-on.

Python learners who want a real, testable project.

Groups of friends/family looking for a simple local turn-based game.

💡 What Makes It Unique

🧠 Interactive learning: Economic concepts emerge naturally from gameplay.

🖥️ No GUI required: Runs entirely in the terminal.

🧩 Modular & extensible: Clean package layout.

🧪 Testing-first: Core rules can be unit-tested with pytest.

🧱 Tech Stack

Python 3.10+

Rich for colors, tables, and layout grids

SQLite for persistence (monopoly.db)

pytest for tests

ruff + black for lint/format

🚀 Getting Started
1) Clone the repository
git clone https://github.com/your-username/monopoly-game-python.git
cd monopoly-game-python
2) Create & activate a virtual environment
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
3) Install dependencies
pip install -U pip
pip install -r requirements.txt
4) Run the game
python main.py
🕹️ How to Play (CLI Flow)

Launch the game; you’ll see a Welcome Screen and an Interactive Tutorial (skippable).

Choose number of players and names.

Each turn:

Roll dice and move.

Resolve the tile (buy, upgrade, pay rent, draw card, tax, jail, etc.).

Game continues until bankruptcy or agreed win condition.

The CLI renders a colorful board snapshot, player dashboard, and action prompts each turn using rich.

🧱 Project Structure
monopoly-game-python/
├── board_manager.py        # Board and property management
├── database.py             # SQLite DB connection and queries
├── game_logic.py           # Core game rules and turn sequence
├── interface_manager.py    # CLI UI, menus, and interactions
├── LICENSE.md              # License file
├── main.py                 # Entry point for running the game
├── monopoly.db             # SQLite database file (game data)
├── player_manager.py       # Player data, actions, and funds
├── __pycache__/            # Compiled Python bytecode
│   ├── board_manager.cpython-312.pyc
│   ├── database.cpython-312.pyc
│   ├── game_logic.cpython-312.pyc
│   ├── interface_manager.cpython-312.pyc
│   └── player_manager.cpython-312.pyc
└── README.md               # Documentation
🧱 CLI Styling (Colors & Grids)

Even though this is a CLI app, it is designed to be interactive and visually appealing:

Grid layouts for board snapshot + player dashboard using rich.layout.

Progress bars/meters for cash, net worth, and jail turns.

Keyboard-friendly prompts (single-key actions when possible).

🧪 Testing & QA

Run tests:

pytest -q
🧱 Contribution Guide

We welcome contributions from developers, designers, and board game enthusiasts!

Workflow

Fork the repo → create your copy on GitHub.

Clone your fork locally.

Branch from development:

git checkout development
git checkout -b your-feature-name

Commit with clear messages:

git commit -m "Add rent calculation to player_manager"

Push & open a Pull Request against development.

🙌 Contributors

🎨 Mark Adrian — Board Manager

🧠 Saleh Abdulwahab — Interface Manager

🕹️ Paul Karime — Player Manager

🏠 Angel Lucy — Game Logic

Thanks to everyone who helped bring the Monopoly Game — Python Edition to life!

📄 License

This project is licensed under the MIT License. You’re free to use, modify, and distribute it with proper attribution.
