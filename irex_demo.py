#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2021-02-18

@author: cook
"""
import irex_functions as irex
import random
from typing import List

# =============================================================================
# Define variables
# =============================================================================
# name program
__NAME__ = 'irex_demo.py'
# give program a version
__VERSION__ = '0.0.1'
# give program a date
__DATE__ = '2021-02-21'


# =============================================================================
# Define functions
# =============================================================================
def main():
    """
    The main chunk of our code

    :return: None
    """
    # ----------------------------------
    # Lets set up some members
    # ----------------------------------
    # Add Rene
    rene = irex.Professor('Rene Doyon', importance=10000)

    # Add Etienne
    etienne = irex.Researcher('Etienne Artigau', importance=999)

    # Add Neil
    neil = irex.PostDoc('Neil Cook', importance=100)

    # Add a student
    bob = irex.Student('Bob', importance=1)

    # add all members to a list
    irex_presenters = [etienne, neil, bob]

    # choose someone to show a plot - and show it
    get_someone_to_show_a_plot(irex_presenters)


def get_someone_to_show_a_plot(presenters: List[irex.IrexMember]):
    """
    Choose someone to show a plot

    :param presenters: list of irex members who are presenters
    :return:
    """
    # get number of presenters
    num_presenters = len(presenters)
    # choose the presenter number
    number = random.choice(list(range(num_presenters)))
    # presenter choosen
    print('\n{0} was choosen'.format(presenters[number].name))
    # someone shows a plot
    presenters[number].show_plot(presenters[number].color)


# =============================================================================
# Start of code
# =============================================================================
if __name__ == "__main__":
    # run main function
    main()

# =============================================================================
# End of code
# =============================================================================
