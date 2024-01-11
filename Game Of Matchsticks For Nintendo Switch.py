def main():
    print(18*"*")
    print("* GAME OF STICKS *")
    print(18*"*")
    print()
    first_choice = input("Type anything to configure the game, press enter "
                         "key to start with default settings: ")
    print()
    players = ""
    sticks = ""
    turn = 0
    if first_choice not in "":
        while True:
            try:
                input_players = int(input("How many players are you? "))
                print()
            except ValueError:
                print("Enter a valid amount of people!")
                print()
                continue
            if input_players > 0:
                players = input_players
                break
            else:
                print("Enter a valid amount of people!")
                print()
        while True:
            try:
                input_sticks = int(input("How many sticks there are? "))
            except ValueError:
                print("Enter a valid amount of sticks!")
                print()
                continue
            if input_sticks > 0:
                sticks = input_sticks
                print()
                break
            else:
                print("Enter a valid amount of sticks!")
                print()
    else:
        players = 2
        sticks = 21
    while True:
        user_input = input(f"Player {turn + 1} enter how many sticks to "
                           f"remove: ")
        if user_input in ("1", "2", "3"):
            removed_sticks = int(user_input)
            sticks -= removed_sticks
            if sticks == 1:
                turn = (turn + 1) % players
                break
            elif sticks <= 0:
                break
            print(f"There are {sticks} sticks left")
            turn = (turn + 1) % players
        else:
            print(f"Must remove between 1-3 sticks!")
    print()
    print(f"Player {turn + 1} lost the game!")


if __name__ == "__main__":
    main()
