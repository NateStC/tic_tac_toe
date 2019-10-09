nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
player1 = 'X'
player2 = 'O'
tiles = {}
xs = []
os = []
wins = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 3], [7, 5, 3], [1, 5, 9]]


def print_v_line():
    print('   |   |   ')


def print_h_line():
    print_v_line()
    print('-' * 11)
    print_v_line()


def print_row(a, b, c):
    print(' ' + tiles[a] + ' | ' + tiles[b] + ' | ' + tiles[c] + ' ')


def reset_board():
    global tiles
    tiles = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def printBoard():
    print_v_line()
    print_row(7, 8, 9)
    print_h_line()
    print_row(4, 5, 6)
    print_h_line()
    print_row(1, 2, 3)
    print_v_line()


def move_input(player):
    legit = False
    global moves
    printBoard()
    print(f"Which spot would you like to place your '{player}'?")
    while not legit:
        i = 0
        move = input()
        if not move.isdigit():  # validate input
            print("Please choose a number")
            i+=1
            break
        else:
            move = int(move)
        if move not in nums:  # validate board slot
            print("Please choose between 1-9 available on the board")
            i+=1
            break
        elif tiles[move] in ['X', 'O']:   # check if tile is available
            print(f'Spot {move} is already taken')
            i+=1
        else:
            tiles[move] = player
            if player == "X":
                xs.append(move)
            else:
                os.append(move)
            print(f'X = {xs}')
            print(f'O = {os}')
            moves += 1
            legit = True
        if i%3 == 0:
            printBoard()


def win_check(player):
    if player == "X":
        spots = xs
    else:
        spots = os
    if spots in wins:
        print(f'{player}s won!')
        return True
    return False


def set_player():
    player_set = False
    while not player_set:
        legit = False
        player = ' '
        while not legit:
            print("Would you like to be 'X' or 'O'?")
            player = input()
            if player.lower() in ['x', 'o']:
                legit = True
        if player.lower() == 'x':
            player_set = True
        else:
            global player1, player2
            player1 = 'O'
            player2 = 'X'
            print("Player1 is 'O'")
            player_set = True


def start_game():
    set_player()
    play_game()


def play_game():
    reset_board()
    game_over = False
    moves = 0
    while not game_over:
        move_input(player1)
        if win_check(player1):
            break
        if moves == 9:
            print("TIE!")
            break
        move_input(player2)
        if win_check(player2):
            break
    print("Play again?")
    again = input()
    if again.lower() in ['yes', 'y', 'sure', 'why not', 'ok', 'okay']:
        play_game()


start_game()
