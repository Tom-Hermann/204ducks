#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## boostrap_grandhog
## File description:
## boostrap
##

from sys import argv
from src.error import error
from src.calcul import get_integral_from_percent, average, standard_deviation, get_integral_from_t
from math import ceil


def main(arg):
    error(arg)
    a = float(arg[1])
    average_time = average(a)
    cb_50 = get_integral_from_percent(a, 0.5)
    cb_99 = get_integral_from_percent(a, 0.99)

    print("Average return time: {}m {}s".format(int(average_time), ceil((average_time - int(average_time)) * 60)))
    print("Standard deviation: {:.3f}".format(standard_deviation(a, average_time)))
    print("Time after which 50% of the ducks are back: {}m {:02d}s".format(int(cb_50 // 60), int(cb_50 - (cb_50 // 60) * 60)))
    print("Time after which 99% of the ducks are back: {}m {:02d}s".format(int(cb_99 // 60), int(cb_99 - (cb_99 // 60) * 60)))
    print("Percentage of ducks back after 1 minute: {:.1%}".format(get_integral_from_t(a, 1)))
    print("Percentage of ducks back after 2 minutes: {:.1%}".format(get_integral_from_t(a, 2)))

if __name__ == "__main__":
    main(argv)
    exit(0)
