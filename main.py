import tictactoe


def main():
    print("Welcome to the Jump Game Console!  ")
    queues = ["Q", "q"]
    selection = ""
    while selection not in queues:
        print("  --- Enter t for TicTacToe ---")
        print("    --- Enter q to quit ---")
        selection = input("What would you like to play? : ")
        if selection == "t":
            tictactoe.play_t3()
        elif selection in queues:
            continue
        else:
            print("INVALID INPUT, TRY AGAIN")


if __name__ == '__main__':
    main()
