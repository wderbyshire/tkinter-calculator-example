import tkinter as tk
import os
from settings import *
from tkinter import font


class CalculatorApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Changes title of the window
        self.title("Calculator")
        self.configure(background="blue")

        self.iconbitmap(default=os.path.join(os.getcwd(), "images", "favicon.ico"))

        self.geometry("{}x{}".format(APP_SIZE[0], APP_SIZE[1]))

        self.input_window = InputFrame(self)
        self.input_window.grid(row=0, rowspan=2, column=0, columnspan=4, sticky=tk.NSEW)

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight=1)


class InputFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.configure(background=INPUT_BACKGROUND)
        self.input_font_size = LARGE_FONT_SIZE

        self.input_label = tk.Label(
            self,
            foreground=INPUT_FOREGROUND_MAIN,
            background=INPUT_BACKGROUND,
            anchor="se",
            text="Hello Marshall",
            font=font.Font(family=FONT_FAMILY, size=LARGE_FONT_SIZE)
        )

        self.input_label.grid(row=0, column=0, sticky=tk.NSEW)
