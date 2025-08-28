from database import setup_database
from interface_manager import main as game_main

if __name__ == "__main__":
    print("=== Welcome to Simple Monopoly ===")
    setup_database()
    game_main()