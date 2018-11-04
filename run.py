#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math
import numpy as np

from core.graph import draw
from methods.all import Exact
from methods.all import Euler
from methods.all import ImprovedEuler
from methods.all import RungeKutta

C = 0.693  # Константа из решения. См. README.md -> Решение
HS = 0.01
HF = 1.01
HH = 0.05
X0 = 0
Y0 = 1
XF = 3


def equation(x, y):
    return 2 * (math.sqrt(y) + y)


def solved_equation(x):
    return (math.exp(x + C) - 1) ** 2


def calculate_error(ys_approx, ys_exact):
    return [abs(y1 - y2) for y1, y2 in zip(ys_approx, ys_exact)]


def calculate_mean_error(ys_approx, ys_exact):
    return sum(calculate_error(ys_approx, ys_exact))/len(ys_exact)


if __name__ == '__main__':
    euler_error = []
    better_euler_error = []
    rk_error = []

    h_axis = np.arange(HS, HF, HH)
    for H in h_axis:
        print(H)
        exact = Exact(solved_equation, H)
        exact_ys = exact.calculate(X0, Y0, XF)

        euler = Euler(equation, H)
        euler_ys = euler.calculate(X0, Y0, XF)

        better_euler = ImprovedEuler(equation, H)
        b_euler_ys = better_euler.calculate(X0, Y0, XF)

        runge_kutta = RungeKutta(equation, H)
        rk_ys = runge_kutta.calculate(X0, Y0, XF)

        # draw(X0, XF, H, ['Exact', 'Euler'], exact_ys, euler_ys)
        # draw(X0, XF, H, ['Exact', 'Improved Euler'], exact_ys, b_euler_ys)
        # draw(X0, XF, H, ['Exact', 'Runge Kutta'], exact_ys, rk_ys)

        euler_error.append(calculate_mean_error(euler_ys, exact_ys))
        better_euler_error.append(calculate_mean_error(b_euler_ys, exact_ys))
        rk_error.append(calculate_mean_error(rk_ys, exact_ys))

    draw(HS, HF, HH, ['Euler', 'Impr Euler', 'Runge Kutta'], euler_error, better_euler_error, rk_error)

    #euler_error = calculate_error(euler_ys, exact_ys)
    #better_euler_error = calculate_error(b_euler_ys, exact_ys)
    #rk_error = calculate_error(rk_ys, exact_ys)

