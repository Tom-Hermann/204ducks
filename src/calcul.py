##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-204ducks-tom.hermann
## File description:
## calcul
##

from math import exp, sqrt

def proba(a, t):
    return a * exp(-t) + (4 - 3 * a) * exp(-2 * t) + (2 * a - 4) * exp(-4 * t)

def average(a):
    result = 0.0
    t = 0.0
    while t < 10:
        result += proba(a, t) * t
        t += 0.001
    return result / 1000

def standard_deviation(a, average_time):
    result = 0.0
    t = 0.0
    while t < 100:
        result += (t - average_time) ** 2 * proba(a, t)
        t += 0.001
    return sqrt(result / 1000)

def get_integral_from_percent(a, percent):
    t = 0.0
    res = 0
    step = 0.001
    while res < percent:
        res += proba(a, t) * step + (proba(a, t + step) - proba(a, t)) * step / 2
        t += step
    return round(t * 60)

def get_integral_from_t(a, t):
    percent = 0
    step = 0.001
    i = 0
    while i < t:
        percent += proba(a, i) * step + (proba(a, i + step) - proba(a, i)) * step / 2
        i += step
    return round(percent * 1000) / 1000


