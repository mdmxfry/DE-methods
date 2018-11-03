#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import os

import numpy as np
import matplotlib.pyplot as plt

if not os.path.isdir('results'):
    os.mkdir('results')

plt.style.use('ggplot')


def draw(x0, xf, h, labels, *args):
    assert len(labels) == len(args)

    xs = np.arange(x0, xf, h)

    for (i, ys) in enumerate(args):
        print(len(xs), len(ys), xs[0], ys[0], xs[-1], ys[-1])
        plt.plot(xs, ys, label=labels[i], linewidth=1)
    plt.xlabel('H')
    plt.ylabel('Y')
    plt.title("Result")
    plt.legend()
    filename = '&'.join(labels).replace(' ', '')  # создаем имя файла по методам что сравнивали и отрезку
    plt.savefig('results/{}_{}-{}.png'.format(filename, x0, xf), dpi=300)
    plt.show()