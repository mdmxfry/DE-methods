#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import math

import numpy as np


class Exact:
    def __init__(self, solved_equation, h):
        self.f = solved_equation
        self.h = h

    def _next_y(self, xi, yi):
        """
        Считает y[i+1] следующим образом:
            y[i+1] = f(x[i+1])

        P.S.
        Функция вынесена таким образом, чтобы в след. методах (классах)
        можно было просто перегрузить ее и получить новый метод не дублируя код.

        :param xi: x[i]
        :param yi: y[i]
        :return: y[i+1]
        """
        return self.f(xi)

    def calculate(self, x0, y0, xf):
        """
        Вычисляет значения на промежуте [x0;xf] с шагом h выражения f

        :param x0:
        :param y0:
        :param xf:
        :return: список значений приближения для промежутка [x0;xf]
        """
        ys = []
        xs = np.arange(x0 + self.h, xf + self.h, self.h)  # вектор всех значений x
        y = y0
        for x in xs:
            ys.append(y)
            y = self._next_y(x, y)
        return ys


class Euler(Exact):
    def _next_y(self, xi, yi):
        """
        Считает y[i+1] исходя из x[i] и y[i] следующим образом:
            y[i+1] = y[i] + h * f(xi, yi)

        :param xi: x[i]
        :param yi: y[i]
        :return: y[i+1]
        """
        return yi + self.h * self.f(xi, yi)


class ImprovedEuler(Euler):
    def _next_y(self, xi, yi):
        """
        Считает y[i+1] исходя из x[i] и y[i] следующим образом:
            y[i+1] = y[i] + h * f(xi + h/2, yi + h/2 * f(xi, yi))

        :param xi: x[i]
        :param yi: y[i]
        :return: y[i+1]
        """
        h2 = self.h / 2
        delta_y = self.h * self.f(xi + h2, yi + h2 * self.f(xi, yi))
        return yi + delta_y


class RungeKutta(Euler):
    def _next_y(self, xi, yi):
        """
        Считает y[i+1] исходя из x[i] и y[i] следующим образом:
            y[i+1] = y[i] + h/6 * (k1 + 2k2+ 2k3 + k4)
            k1 = f(xi, yi)
            k2 = f(xi + h/2, yi + h/2 * k1)
            k3 = f(xi + h/2, yi + h/2 * k2)
            k4 = f(xi + h, yi + h * k3)

        :param xi: x[i]
        :param yi: y[i]
        :return: y[i+1]
        """
        h2 = self.h / 2
        k1 = self.f(xi, yi)
        k2 = self.f(xi + h2, yi + h2 * k1)
        k3 = self.f(xi + h2, yi + h2 * k2)
        k4 = self.f(xi + self.h, yi + self.h * k3)
        return yi + (self.h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
