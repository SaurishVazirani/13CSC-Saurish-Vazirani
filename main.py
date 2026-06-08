import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading
from datetime import datetime
from PIL import Image, ImageTk
import os, sys

#paths/image list
BASE = os.path.dirname(os.path.abspath(__file__))

ASSETS = {
    #dumbell image
    "dumbell_3d_L": "Images/png/Dumbell_L.png",
    "dumbell_3d_R": "Images/png/Dumbell_R.png",
    #White Navbar Buttons
    "Nav_home_w": "Images/png/Home Navbar.png",
    "Nav_dumbell_w": "Images/png/Dumbell Navbar.png",
    "Nav_log_w": "Images/png/Log Navbar.png",
    #Black Navbar Buttons
    "Nav_home_b": "Images/png/Home Navbar Black.png",
    "Nav_dumbell_b": "Images/png/Dumbell Navbar Black.png",
    "Nav_log_b": "Images/png/Log Navbar Black.png",
    #other images
    "Stopwatch": "Images/png/Stopwatch.png",
    "Scale": "Images/png/Scale.png",
}

#list for colours
BG_LIGHT = "#99c5ff"
BG_NAV = "#3770df"
BTN_BG = "#000000"
BTN_FG = "ffffff"
TEXT_DARK = "000000"
TEXT_NAV = "ffffff"

W, H = 1400, 780
Nav_H = 110



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RepFit")
        self.resizable(False, False)
        self.geometry(f"{W}x{H}")
        self.configure(bg=BG_LIGHT)

        self.fonts = {
            "title": tkfont.Font(family="Impact", size=62, weight="Bold")
        }