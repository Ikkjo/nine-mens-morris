from services.gameboard_service import GameboardService


def next_move_menu():
    show_gameboard()
    piece = piece_input()
    next_move = position_input()

def position_input():
    return input("Unesite poziciju na koju zelite da se pomerite\n>>>\n\n")



def piece_input():
    return input("Unesite poziciju figure koju zelite da pomerite\n>>>\n\n")


def show_gameboard():
    print(GameboardService().gameboard)

if __name__ == '__main__':
    show_gameboard()