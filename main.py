from game import game, debug
import sys

if __name__ == '__main__':

    if sys.argv[0].upper() == "DEBUG":
        debug()
    else:
        game()
