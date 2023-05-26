# Size
APP_SIZE = (400, 700)
MAIN_ROWS = 8
MAIN_COLUMNS = 4

# Styling
STANDARD_PAD = {"padx": 2, "pady": 2}

NUM_BUTTONS = {
    "0": {"image": "0.png", "value": "0", "position": {"column": 0, "columnspan": 2, "row": 7}},
    ".": {"image": "point.png", "value": ".", "position": {"column": 2, "row": 7}},
    "1": {"image": "1.png", "value": "1", "position": {"column": 0, "row": 6}},
    "2": {"image": "2.png", "value": "2", "position": {"column": 1, "row": 6}},
    "3": {"image": "3.png", "value": "3", "position": {"column": 2, "row": 6}},
    "4": {"image": "4.png", "value": "4", "position": {"column": 0, "row": 5}},
    "5": {"image": "5.png", "value": "5", "position": {"column": 1, "row": 5}},
    "6": {"image": "6.png", "value": "6", "position": {"column": 2, "row": 5}},
    "7": {"image": "7.png", "value": "7", "position": {"column": 0, "row": 4}},
    "8": {"image": "8.png", "value": "8", "position": {"column": 1, "row": 4}},
    "9": {"image": "9.png", "value": "9", "position": {"column": 2, "row": 4}}
}

ARITHMETIC_OP_BUTTONS = {
    "multiply": {"image": "multiply.png", "character": "×", "operation": "*", "position": {"column": 3, "row": 3}},
    "divide": {"image": "divide.png", "character": "÷", "operation": "/", "position": {"column": 3, "row": 2}},
    "add": {"image": "add.png", "character": "+", "operation": "+", "position": {"column": 3, "row": 5}},
    "subtract": {"image": "subtract.png", "character": "-", "operation": "-", "position": {"column": 3, "row": 4}},
    "mod": {"image": "mod.png", "character": "MOD", "operation": "%", "position": {"column": 1, "row": 3}},
    "power": {"image": "power.png", "character": "^", "operation": "**", "position": {"column": 2, "row": 3}},
}

OP_BUTTONS = {
    "backspace": {"image": "back_s.png", "position": {"column": 0, "row": 2}},
    "clear": {"image": "c.png", "position": {"column": 1, "row": 2}},
    "clear_all": {"image": "ce.png", "position": {"column": 2, "row": 2}},
    "invert": {"image": "invert.png", "position": {"column": 0, "row": 3}},
    "equals": {"image": "equals.png", "position": {"column": 3, "row": 6, "rowspan": 2}},
}

# Colours
MAIN_BACKGROUND = "#66bcde"

INPUT_BACKGROUND = "#e8e8e8"
INPUT_FOREGROUND_MAIN = "#2b2b2b"
INPUT_FOREGROUND_SECONDARY = "#636363"

BUTTON_COLORS = {
    "numbers": {"main": "#303AAB", "hovered": "#3A46B6", "selected": "#2D3A6E", "foreground": "#E1E1E1"},
    "arith_op": {"main": "#C17126", "hovered": "#CE853E", "selected": "#996D3F", "foreground": "#E1E1E1"},
    "standard_op": {"main": "#3C4058", "hovered": "#4C5065", "selected": "#393840", "foreground": "#E1E1E1"},
    "equals": {"main": "#CD362B", "hovered": "#D7473F", "selected": "#A84743", "foreground": "#E1E1E1"},
}

# Fonts
FONT_FAMILY = "Segoe UI"
LARGE_FONT_SIZE = 30
SMALL_FONT_SIZE = 15
