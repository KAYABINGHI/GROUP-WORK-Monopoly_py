# runs the game loop & CLI interface


def main():
    setup_database()
    players = load_players()
    ownership = load_ownerships()

    if not players: # if no players, set up new game
        num = int(input("How many players? ")) # get number of players
        for i in range(num):
            name = input(f"Enter name for player {i + 1}: ")
            players.append({ # create a new player dict
                "name": name,
                "balance": 1500,
                "position": 0, # strats at Go tile
                "in_jail": 0, # not in jail at start
            }) # sets the default starting values