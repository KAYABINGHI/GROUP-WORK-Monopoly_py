from board_manager import display_board
from player_manager import setup_database, load_players, save_players, load_ownership, save_ownership
from game_logic import roll_dice, move_player, handle_space

def create_players():
    players = []
    num = int(input("How many players? (2-4): "))
    for i in range(num):
        name = input(f"Enter name for Player {i+1}: ")
        players.append({"name": name, "balance": 1500, "position": 0, "in_jail": 0})
    return players

def remove_bankrupt(players):
    return [p for p in players if p["balance"] > 0]

def check_winner(players):
    if len(players) == 1:
        print(f"\n{players[0]['name']} wins the game with ${players[0]['balance']}!")
        return True
    return False
def take_turn(player, players, ownership):
    if player["in_jail"]:
        print(f"{player['name']} is in Jail! Skips this turn.")
        player["in_jail"] = 0
        return
    input(f"{player['name']}, press Enter to roll dice...")
    d1, d2, doubles = roll_dice()
    print(f"Rolled {d1} and {d2} (total {d1 + d2})")
    move_player(player, d1 + d2)
    handle_space(player, players, ownership)