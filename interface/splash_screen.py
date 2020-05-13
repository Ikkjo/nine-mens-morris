from time import sleep

from interface.ascii_art import art


def splash_screen():
    made_by = "Ilija Kalinić"
    game_name = "Nine Men's Morris"
    print("{0:#^60}\nMade by:{1:#>52}".format(game_name, made_by))
    print("{:^60}".format(art))
    sleep(5)