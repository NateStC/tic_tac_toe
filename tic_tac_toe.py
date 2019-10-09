import random

player1 = 'X'
player2 = 'O'
tiles = {}
wins = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2],
        [9, 6, 3], [7, 5, 3], [1, 5, 9]]


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


def print_board():
    print_v_line()
    print_row(7, 8, 9)
    print_h_line()
    print_row(4, 5, 6)
    print_h_line()
    print_row(1, 2, 3)
    print_v_line()


def move_input(player):
    legit = False
    while not legit:
        print_board()
        move = input(f"Which spot would you like to place your '{player}'?\n")
        if not move.isdigit():  # validate input is a number
            print_board()
            print("Please choose a number")
        else:
            move = int(move)
        if move not in range(1, 10):  # validate board slot
            print_board()
            print("Please choose between 1-9 available on the board")
        elif tiles[move] in ['X', 'O']:   # check if tile is available
            print_board()
            print(f'Spot {move} is already taken')
        else:
            tiles[move] = player
            legit = True


def win_check(player):
    for w in wins:
        if tiles[w[0]] == tiles[w[1]] == tiles[w[2]] == player:
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


def coinFlip():
    flip = random.randint(0, 1)
    if flip == 0:
        return player1
    else:
        return player2


def play_game():
    reset_board()
    game_over = False
    moves = 0
    player = coinFlip()
    while not game_over:
        if player == player1:  # switch turn to other player
            player = player2
        else:
            player = player1
        move_input(player)
        moves += 1
        if win_check(player):
            print_board()
            print(f'{player} won!')
            game_over = True
        elif moves == 9:
            print("TIE!")
            game_over = True
    again = input("Play again?\n")
    if again.lower() in ['yes', 'y', 'sure', 'why not', 'ok', 'okay']:
        play_game()


start_game()
