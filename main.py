import tkinter as tk
from tkinter import font as tkfont
import math

#list for colours

BG_LIGHT = "#99c5ff"
BG_NAV = "#3770df"
BTN_BG = "#000000"
BTN_FG = "ffffff"
TEXT_DARK = "000000"
TEXT_NAV = "ffffff"

W, H = 480, 320

class App(tk.TK):
    def __init__(self):
        super().__init__()
        self.title("RepFit")
        self.resizable(False, False)
        self.geometry(f"{W}x{H}")
        self.configure(bg=BG_LIGHT)

        self.fonts = {
            "title": tkfont.Font(family="Impact", size=62, weight="Bold")
        }