#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math

from methods.all import Exact
from methods.all import Euler
from methods.all import ImprovedEuler
from methods.all import RungeKutta

C = 0.693  # Константа из решения. См. README.md -> Решение
H = 0.04


def equation(x, y):
    return 2 * (math.sqrt(y) + y)


def solved_equation(x):
    return (math.exp(x + C) - 1) ** 2


if __name__ == '__main__':
    exact = Exact(solved_equation, H)
    print(exact.calculate(0, 1, 9))

    euler = Euler(equation, H)
    print(euler.calculate(0, 1, 9))

    better_euler = ImprovedEuler(equation, H)
    print(better_euler.calculate(0, 1, 9))

    runge_kutta = RungeKutta(equation, H)
    print(runge_kutta.calculate(0, 1, 9))
