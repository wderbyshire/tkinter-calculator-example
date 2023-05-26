import tkinter as tk
import os
from settings import *


class CalculatorApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Changes title of the window
        self.title("Calculator")

        #
        self.iconbitmap(default=os.path.join(os.getcwd(), "images", "favicon.ico"))

        self.geometry("{}x{}".format(APP_SIZE[0], APP_SIZE[1]))

