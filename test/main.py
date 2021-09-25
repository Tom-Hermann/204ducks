#!/usr/bin/python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-204ducks-tom.hermann
## File description:
## main
##

import unittest
from math import ceil
from src.calcul import *
from src.main import main
import sys

class TestStringMethods(unittest.TestCase):

    def test_proba(self):
        self.assertEqual(proba(1.6, 1), 0.46568636817403014)
        self.assertEqual(proba(0.2, 1), 0.4677795512393286)

    def test_average(self):
        average_time = average(1.6)
        self.assertEqual(int(average_time), 1)
        self.assertEqual(ceil((average_time - int(average_time)) * 60), 21)
        average_time = average(0.2)
        self.assertEqual(int(average_time), 0)
        self.assertEqual(ceil((average_time - int(average_time)) * 60), 50)

    def test_standart_deviation(self):
        sd = standard_deviation(1.6, average(1.6))
        self.assertEqual("{:.3f}".format(sd), "1.074")
        sd = standard_deviation(0.2, average(0.2))
        self.assertEqual("{:.3f}".format(sd), "0.676")

    def test_integral_from_percent(self):
        integral = get_integral_from_percent(1.6, 0.5)
        time = "{}m {:02d}s".format(int(integral // 60), int(integral - (integral // 60) * 60))
        self.assertEqual(time, "1m 04s")
        integral = get_integral_from_percent(1.6, 0.99)
        time = "{}m {:02d}s".format(int(integral // 60), int(integral - (integral // 60) * 60))
        self.assertEqual(time, "5m 04s")


        integral = get_integral_from_percent(0.2, 0.5)
        time = "{}m {:02d}s".format(int(integral // 60), int(integral - (integral // 60) * 60))
        self.assertEqual(time, "0m 39s")
        integral = get_integral_from_percent(0.2, 0.99)
        time = "{}m {:02d}s".format(int(integral // 60), int(integral - (integral // 60) * 60))
        self.assertEqual(time, "3m 16s")

    def test_integral_from_t(self):
        pourcent = "{:.1%}".format(get_integral_from_t(1.6, 1))
        self.assertEqual(pourcent, "46.9%")
        pourcent = "{:.1%}".format(get_integral_from_t(1.6, 2))
        self.assertEqual(pourcent, "79.1%")
        pourcent = "{:.1%}".format(get_integral_from_t(0.2, 1))
        self.assertEqual(pourcent, "71.3%")
        pourcent = "{:.1%}".format(get_integral_from_t(0.2, 2))
        self.assertEqual(pourcent, "94.2%")



if __name__ == '__main__':
    unittest.main()