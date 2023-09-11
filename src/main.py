import sys
import os
import pygame

import tailwind.window
import tailwind.util as util

def onTick(_window: tailwind.window.Window, *args, **kwargs):
    pass

window = tailwind.window.Window(None, "Maths CAT Investigation", util.WindowProperties.empty(), debug=True, onTick=onTick)


