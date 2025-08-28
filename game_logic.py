# game_logic.py
# Core rules of Monopoly

import random
from .board_manager import BOARD, PROPERTY_PRICES, RENT, TAXES
from .player_manager import save_players, save_ownership

CHANCE_CARDS = [
    ("Bank pays you dividend", +50),
    ("Doctor's fee, pay", -50),
    ("Advance to GO", "GO"),
    ("Go back 3 spaces", -3)
]

COMMUNITY_CARDS = [
    ("Inherit $100", +100),
    ("Pay hospital $100", -100),
    ("Advance to GO", "GO"),
    ("Go to Jail", "Jail")
]

def roll_dice():
    d1, d2 = random.randint(1,6), random.randint(1,6)
    return d1, d2, (d1 == d2)

def move_player(player, steps):
    player["position"] = (player["position"] + steps) % len(BOARD)
    if player["position"] == 0:  # Passed GO
        player["balance"] += 200

def handle_space(player, players, ownership):
    space = BOARD[player["position"]]

    # Taxes
    if space in TAXES:
        player["balance"] -= TAXES[space]
        print(f"{player['name']} pays {TAXES[space]} for {space}.")

    # Properties
    elif space in PROPERTY_PRICES:
        if space not in ownership:
            choice = input(f"{player['name']}, buy {space} for ${PROPERTY_PRICES[space]}? (y/n): ").lower()
            if choice == "y" and player["balance"] >= PROPERTY_PRICES[space]:
                player["balance"] -= PROPERTY_PRICES[space]
                ownership[space] = player["name"]
                print(f"{player['name']} bought {space}.")
        else:
            owner = ownership[space]
            if owner != player["name"]:
                rent = RENT[space]
                player["balance"] -= rent
                for p in players:
                    if p["name"] == owner:
                        p["balance"] += rent
                print(f"{player['name']} pays ${rent} rent to {owner}.")
