import datetime
BOARD = {1: ' ',  2: ' ',  3: ' ',
         4: ' ',  5: ' ',  6: ' ',
         7: ' ',  8: ' ',  9: ' '}
PLAYED_SQUARES = []

def print_t3(victor_message):
    theTime = datetime.datetime.now().strftime("%m/%d/%Y @ %H:%M")
    winnerEntry = f"\n{victor_message} on {theTime}"
    try:
        winnerFile = open("winnerFile.txt", "x")
        winnerFile.writelines(str(winnerEntry))
    except FileExistsError:
        winnerFile = open("winnerFile.txt", "a")
        winnerFile.writelines(str(winnerEntry))
    finally:
        winnerFile.close()


def render():
    board_state = f"""    {BOARD[1]} | {BOARD[2]} | {BOARD[3]}
    --+---+--
    {BOARD[4]} | {BOARD[5]} | {BOARD[6]}
    --+---+--
    {BOARD[7]} | {BOARD[8]} | {BOARD[9]}"""
    print(board_state)


def get_action(player):
    acceptable = False
    while acceptable is False:
        try:
            action = int(input(f"Player {player}, please enter an Integer between 1 and 9: "))
            if action not in range(1, 10):
                raise ValueError
            if action in PLAYED_SQUARES:
                raise TypeError
            else:
                PLAYED_SQUARES.append(action)
        except TypeError:
            print("That box is taken...")
        except ValueError:
            print("Please enter an INTEGER BETWEEN 1 and 9.")
        else:
            acceptable = True
            return action


def victory_message(player):
    message_of_victory = f"Player {player} won TicTacToe"
    print(message_of_victory)
    print_t3(message_of_victory)


def check_win(player):
    winnerFound = False
    String1 = f"{player}{player}{player}"
    row1 = f"{BOARD[1]}{BOARD[2]}{BOARD[3]}"
    row2 = f"{BOARD[4]}{BOARD[5]}{BOARD[6]}"
    row3 = f"{BOARD[7]}{BOARD[8]}{BOARD[9]}"
    column1 = f"{BOARD[1]}{BOARD[4]}{BOARD[7]}"
    column2 = f"{BOARD[2]}{BOARD[5]}{BOARD[8]}"
    column3 = f"{BOARD[3]}{BOARD[6]}{BOARD[9]}"
    diagonal1 = f"{BOARD[1]}{BOARD[5]}{BOARD[9]}"
    diagonal2 = f"{BOARD[3]}{BOARD[5]}{BOARD[7]}"
    stringsToCheck = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
    for s in stringsToCheck:
        if s == String1:
            winnerFound = True
            victory_message(player)
            break
    return winnerFound


def play_t3():
    game_round = 0
    game_over = False
    while not game_over:
        render()
        if game_round % 2 > 0:
            player = "O"
        else:
            player = "X"
        square = get_action(player)
        BOARD[square] = player
        game_round += 1
        if  game_round >= 5:
            game_over = check_win(player)
        if (game_round == 9) and (game_over is False):
            player = "TIE GAME"
            print(player)
            print_t3(player)
            game_over = True
    restart = input("Would you like to play again?  Enter 1 for YES or anything else for NO: ")
    if restart == "1":
        for x in BOARD:
            BOARD[x] = ' '
            PLAYED_SQUARES.clear()
        play_t3()
    print(" ")
