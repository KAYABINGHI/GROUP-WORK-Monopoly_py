# Handles the 40-space Monopoly board

BOARD = [
    "GO",
    "Mediterranean Avenue", "Community Chest", "Baltic Avenue", "Income Tax",
    "Reading Railroad",
    "Oriental Avenue", "Chance", "Vermont Avenue", "Connecticut Avenue",
    "Jail",
    "St. Charles Place", "Electric Company", "States Avenue", "Virginia Avenue",
    "Pennsylvania Railroad",
    "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue",
    "Free Parking",
    "Kentucky Avenue", "Chance", "Indiana Avenue", "Illinois Avenue",
    "B&O Railroad",
    "Atlantic Avenue", "Ventnor Avenue", "Water Works", "Marvin Gardens",
    "Go To Jail",
    "Pacific Avenue", "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", 
      "Short Line Railroad",
    "Chance", "Park Place", "Luxury Tax", "Boardwalk"
]

PROPERTY_PRICES = {
    "Mediterranean Avenue": 60, "Baltic Avenue": 60,
    "Oriental Avenue": 100, "Vermont Avenue": 100, "Connecticut Avenue": 120,
    "St. Charles Place": 140, "States Avenue": 140, "Virginia Avenue": 160,
    "St. James Place": 180, "Tennessee Avenue": 180, "New York Avenue": 200,
    "Kentucky Avenue": 220, "Indiana Avenue": 220, "Illinois Avenue": 240,
    "Atlantic Avenue": 260, "Ventnor Avenue": 260, "Marvin Gardens": 280,
    "Pacific Avenue": 300, "North Carolina Avenue": 300, "Pennsylvania Avenue": 320,
    "Park Place": 350, "Boardwalk": 400
}

RENT = {prop: price // 5 for prop, price in PROPERTY_PRICES.items()}

TAXES = {"Income Tax": 200, "Luxury Tax": 100}

def display_board(players):
    #display of board with player positions
    print("\n=== Monopoly Board (Positions) ===")
    for i, space in enumerate(BOARD): #enumerate gives index and value(o0 to 39)
        marks = [] 
        for p in players: 
            if p["position"] == i: #if player is on the current space
                marks.append(p["name"][0])  # show first letter of the player's name
        mark_str = " ".join(marks)  # combine all letters into a string (if multiple players on same space)
        print(f"{i:2d}: {space:25} {mark_str}")
    print("==================================\n")
