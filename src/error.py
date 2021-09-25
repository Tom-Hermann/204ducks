##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-204ducks-tom.hermann
## File description:
## error
##

from sys import stderr

def print_usage():
    print("USAGE")
    print("\t./204ducks a\n")
    print("DESCRIPTION")
    print("\ta\tconstant")

def error(argv):
    if (len(argv) ==  2 and (argv[1] == "-h" or argv[1] == "--help")):
        print_usage()
        exit(0)
    elif (len(argv) != 2):
        print_usage()
        exit(84)
    else:
        try:
            float(argv[1])
        except ValueError:
            print("Argument must be an number between 0 and 2.5", file=stderr)
            exit(84)
        if (float(argv[1]) < 0 or float(argv[1]) > 2.5):
            print("Argument must be an number between 0 and 2.5", file=stderr)
            exit(84)