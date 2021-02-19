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
import random
import time
from typing import Union

import misc

# =============================================================================
# Define variables
# =============================================================================
class IrexMember:

    name: str
    mood: Union[str, None]
    color: str = 'green'

    def __init__(self, name: str, importance: Union[int, None] = None):
        """
        Construct an irex member

        :param name: name of irex member
        :param importance: level of importance in the food chain
        """
        # deal with no importance set
        if importance is None:
            importance = 0
        self.name = name
        self.mood = None
        self.importance = importance
        self.is_permanent = False
        # print that someone now exists
        print(self.__str__())

    def __str__(self) -> str:
        msg = '\n {0} exists!'.format(self.name)
        return misc.colourize(msg, self.color)

    def attend_meetings(self):
        """
        Attend a meeting
        :return:
        """
        if self.mood == 'uninterested':
            time.sleep(3600)

    def attend_cafe_irex(self):
        """
        Attend a meeting
        :return:
        """
        if True:
            self.mood = 'Entertained'

    def show_plot(self, color=None):
        fig, frames = plt.subplots(ncols=2, nrows=1)
        frames = misc.fancy_plot(frames, color, self.name)
        plt.show()
        plt.close()


class Professor(IrexMember):
    def __init__(self, name: str, importance: Union[int, None] = None):
        """
        A Professor is an important person

        :param name: name of professor
        """
        # set color
        self.color = 'red'
        # deal with no importance set
        if importance is None:
            importance = 1000
        # call to super class
        super().__init__(name, 1000)


    def chair_meeting(self):
        """
        Chair a meeting

        :return:
        """
        self.importance += 100


class Researcher(IrexMember):
    def __init__(self, name, importance: Union[int, None] = None):
        """
        A Research is probably hard at work

        :param name:
        :param importance:
        """
        # set color
        self.color = 'blue'
        # deal with no importance set
        if importance is None:
            importance = 100
        # call to super class
        super().__init__(name, importance)
        # is permanent
        self.is_permanent = False


    def find_permanent_position(self):
        """
        Find a permanent position
        :return:
        """
        if random.uniform(0, 1) > 0.3:
            self.is_permanent = True
        else:
            self.is_permanent = False
        # return this?
        return self.is_permanent


class PostDoc(Researcher):
    def __init__(self, name, importance: Union[int, None] = None):
        """
        A Research is probably hard at work

        :param name:
        :param importance:
        """
        # call to super class
        super().__init__(name, importance)
        # set color
        self.color = 'magenta'

    def find_permanent_position(self):
        """
        Find a permanent position
        :return:
        """
        # This is going to take a while
        while 1:
            continue
        # return False always
        return False

    def study_fish(self):
        """
        Cafe Irex Material?
        :return:
        """
        if self.name == 'Daniel':
            if random.uniform(0, 1) > 0.5:
                self.study_fish()
            else:
                time.sleep(complex(0, 1))


class Student(IrexMember):
    def __init__(self, name, importance=10):
        """
        The lowly student

        :param name: does it even matter?
        :param importance: not very high
        """
        # set color
        self.color = 'yellow'
        # call to super class
        super().__init__(name, importance)


# =============================================================================
# Define functions
# =============================================================================


# =============================================================================
# Start of code
# =============================================================================
if __name__ == "__main__":
    # print hello world
    print('Hello World')

# =============================================================================
# End of code
# =============================================================================