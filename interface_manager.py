# runs the game loop & CLI interface

# imports
from board_manager import display_board
from player_manager import setup_database, load_players, save_players, load_ownerships, save_ownerships
from game_logic import roll_dice, move_player, handle_space


def main():
    setup_database()
    players = load_players()
    ownership = load_ownerships()

    if not players: # if no players, set up new game
        num = int(input("How many players? ")) # get number of players
        for i in range(num):
            name = input(f"Enter name for player {i + 1}: ") # when displaying, start count at 1 =>{i +1}
            players.append({ # create a new player dict
                "name": name,
                "balance": 1500,
                "position": 0, # strats at Go tile
                "in_jail": 0, # not in jail at start
            }) # sets the default starting values

    turn = 0
    while True:
        display_board(players)    # show the board state
        player = players[turn % len(players)] # picks current player
        print(f"\n{player['name']}'s turn. Balance: ${player['balance']}") # show whose turn it is

        if player["in_jail"]:
            print(f"{player['name']} is in jail! Skips this turn.") 
            player["in_jail"] = 0 # skip turn, release from jail next turn
        else:
            input("Press Enter to roll the dice...")
            d1, d2, doubles = roll_dice()
            print(f"Rolled {d1} and {d2} (total {d1 + d2})")
            move_player(player, d1 + d2) # move the player
            handle_space(player, players, ownership) # handles what happens depending on the space landed on(e.g go to jail)
        if doubles:
                print("Doubles! Roll again.")
                continue # makes the loop repeat for another turn of the same player
        save_players(players) # save the game state
        save_ownerships(ownership)

        turn += 1 # next player's turn

if __name__ == "__main__": 
    main() # start the game loop
