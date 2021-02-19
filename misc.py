#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2021-02-18

@author: cook
"""
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Define variables
# =============================================================================
COLOURS = dict()
COLOURS['BLACK'] = '\033[90;1m'
COLOURS['RED'] = '\033[1;91;1m'
COLOURS['GREEN'] = '\033[92;1m'
COLOURS['YELLOW'] = '\033[1;93;1m'
COLOURS['BLUE'] = '\033[94;1m'
COLOURS['MAGENTA'] = '\033[1;95;1m'
COLOURS['CYAN'] = '\033[1;96;1m'
COLOURS['WHITE'] = '\033[97;1m'
COLOURS['ENDC'] = '\033[0;0m'


# =============================================================================
# Define functions
# =============================================================================
def colourize(message: str, color: str = 'green') -> str:
    """
    Colours a message

    :param message: the message
    :param color: the colour

    :return: str the coloured message
    """
    return COLOURS[color.upper()] + message + COLOURS['ENDC']


def fancy_plot(frames: list, color: str,
               name: str) -> list:
    """
    Adds a "fancy" plot

    :param frames: list of matplotlib.axis

    :return: list of matplotlib.axis
    """
    # Fixing random state for reproducibility
    # np.random.seed(19680801)
    # random data
    dt = 0.01
    t = np.arange(0, 10, dt)
    nse = np.random.randn(len(t))
    r = np.exp(-t / 0.05)
    cnse = np.convolve(nse, r) * dt
    cnse = cnse[:len(t)]
    s = 0.1 * np.sin(2 * np.pi * t) + cnse
    # a plot that Etienne may produce
    frames[0].plot(t, s, color=color)
    frames[1].psd(s, 512, 1 / dt, color=color)

    plt.suptitle('{0}\'s plot'.format(name))
    # return frames (not really necessary)
    return frames


# =============================================================================
# Start of code
# =============================================================================
if __name__ == "__main__":
    # print hello world
    print('Hello World')

# =============================================================================
# End of code
# =============================================================================
