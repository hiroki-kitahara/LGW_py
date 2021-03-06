#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cell_manager import *
from repeated_timer import *
from user_settings import *
import math
from preset_cell import *
from application import *

class UserInput:
    def __init__(self, cellManager, canvas):
        self.cellManager = cellManager
        self.canvas = canvas
        self.canvas.bind("<Button-1>", self.clicked_left_mouse_button)
        self.canvas.bind("<B1-Motion>", self.drag_left_mouse_button)
        self.canvas.bind("<Key>", self.any_key_down)
        self.next_generation_schedule = None

    def next_generation(self):
        self.cellManager.next_generation()
        self.next_generation_schedule = Application().register_schedule(UserSettings.interval(), self.next_generation)
        print(self.next_generation_schedule)

    def clicked_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        x = math.floor(event.x / size)
        y = math.floor(event.y / size)
        if self.cellManager.get_alive(x, y) == False:
            self.cellManager.set_alive(x, y, True)

    def drag_left_mouse_button(self, event):
        size = UserSettings.cell_size()
        x = math.floor(event.x / size)
        y = math.floor(event.y / size)
        if self.cellManager.get_alive(x, y) == False:
            self.cellManager.set_alive(x, y, True)
    
    def any_key_down(self, event):
        keyCode = event.char
        if keyCode == ' ':
            self.cellManager.next_generation()
        if keyCode == 'q':
            self.cellManager.remove_all_cell()
        if keyCode == 'w':
            for y in range(self.cellManager.height):
                for x in range(self.cellManager.width):
                    self.cellManager.set_alive(x, y, True)
        if keyCode == 'z' and self.next_generation_schedule is None:
            self.next_generation()
        if keyCode == 'x' and self.next_generation_schedule is not None:
            Application().cancel_schedule(self.next_generation_schedule)
            self.next_generation_schedule = None
        if keyCode == 'c':
            PresetCell.apply_from_string(self.cellManager, '0123456789/:', 0, 0, 1)




