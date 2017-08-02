#!/usr/bin/env python2
# -*- coding:utf-8 -*-

"""
Graphic network graph.

Displays a simple network graph representing how fast your ping is. This tool
is useful for people having some random connection and looking for a tool to
represent the state of their ping.
"""

from tkinter import *
import socket
import threading
import random
import time
import subprocess

__author__ = "Axel Martin"
__copyright__ = "Copyright 2016, Axel Martin"
__credits__ = ["Axel Martin"]
__licence__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Axel Martin"
__status__ = "Prototype"


class Config:
    """Configuration container."""
    hostname = "foobar.fr"
    updater_rate = 5 # in milliseconds
    ticks = 2
    low_bound, high_bound = 50, 100

class Pingger:
    """Ping tool.

    The purpose of this class is to give abstraction of the ping command line.
    """

    def __init__(self, config):
        self.config = config

        self.reseted = False

        self.alive = True
        self.thread = threading.Thread(target=self.pinger)
        self.thread.start()

    def has_been_reset(self):
        if self.reseted:
            self.reseted = False
            return True
        return False

    def stop(self):
        self.alive = False

    def pinger(self):
        while True:
            subprocess.check_output(["ping", "-n", "1", self.config.hostname])
            self.reseted = True


class App:
    """Tkinter application handler

    Create the window and manage the display on the canvas.
    """

    HEIGHT, WIDTH = 75, 75

    def __init__(self, config):
        self.config = config

        # Interface setup
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.canvas.create_line(0, self.config.low_bound, self.WIDTH - 1, self.config.low_bound, fill="orange", width=2)

        # Drawer helper
        self.pingger = Pingger(self.config)
        self.last_tick_height = 0

        # Updater setup
        self.alive = True
        self.thread = threading.Thread(target=self.update)
        self.thread.start()

    def update(self):
        for offset in range(self.config.ticks + 1, 1, -1):
            self.draw_line(offset)

        # Lines moving
        lines = list(self.canvas.find_withtag("spike"))
        while len(lines) > self.WIDTH:
            self.canvas.delete(lines.pop(0))
        for l in lines:
            x0, y0, x1, y1 = self.canvas.coords(l)
            self.canvas.coords(l, x0 - self.config.ticks, y0, x1 - self.config.ticks, y1)

        # Recall in 10ms
        if self.alive:
            self.root.after(self.config.updater_rate, self.update)

    def draw_line(self, offset):
        if self.pingger.has_been_reset():
            self.last_tick_height = 0
        self.last_tick_height += 1

        if self.last_tick_height * self.config.updater_rate < self.config.low_bound:
            fill = "green"
        elif self.last_tick_height * self.config.updater_rate > self.config.high_bound:
            fill = "red"
        else:
            fill = "orange"

        self.canvas.create_line(self.WIDTH - offset, self.HEIGHT - 1, self.WIDTH - offset,
            self.HEIGHT - self.last_tick_height, tag="spike", fill=fill)

    def stop(self):
        self.alive = False
        self.pingger.stop()

    def start(self):
        self.root.mainloop()

c = Config()
a = App(c)
a.start()

# Passing this point the application closed.
a.stop()