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
    "dumbell_3d_L": "Dumbell_L.png",
    "dumbell_3d_R": "Dumbell_R.png",
    #White Navbar Buttons
    "Nav_home_w": "Home Navbar.png",
    "Nav_dumbell_w": "Dumbell Navbar.png",
    "Nav_log_w": "Log Navbar.png",
    #Black Navbar Buttons
    "Nav_home_b": "Home Navbar Black.png",
    "Nav_dumbell_b": "Dumbell Navbar Black.png",
    "Nav_log_b": "Log Navbar Black.png",
    #other images
    "Stopwatch": "Stopwatch.png",
    "Scale": "Scale.png",
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

def load(name: str, size: tuple) -> ImageTk.PhotoImage:
    path = os.path.join(BASE, ASSETS[name])
    img  = Image.open(path).convert("RGBA").resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

def nav_btn(parent, text, icon_normal, icon_hover, cmd):
    #Return a frame that behaves like a nav button with hover effect.
    frm = tk.Frame(parent, bg=BG_NAV, cursor="hand2")
    lbl_icon = tk.Label(frm, image=icon_normal, bg=BG_NAV)
    lbl_icon.pack()
    lbl_text = tk.Label(frm, text=text, fg=TEXT_W, bg=BG_NAV,
                        font=("Arial", 13, "bold"))
    lbl_text.pack()

    def on_enter(_):
        frm.configure(bg="#4a6ae8")
        lbl_icon.configure(bg="#4a6ae8")
        lbl_text.configure(bg="#4a6ae8")

    def on_leave(_):
        frm.configure(bg=BG_NAV)
        lbl_icon.configure(bg=BG_NAV)
        lbl_text.configure(bg=BG_NAV)

    for w in (frm, lbl_icon, lbl_text):
        w.bind("<Enter>", on_enter)
        w.bind("<Leave>", on_leave)
        w.bind("<Button-1>", lambda e:cmd())
    return frm

class RepFitApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RepFit")
        self.resizable(False, False)
        self.geometry(f"{W}x{H}")
        self.configure(bg=BG_LIGHT)

        #Storing workout logs
        self.workout_log: list[dict] = []

        self._load_images()
        self._build_ui()
        self.show_home()

    #loading images
    def _load_images(self):
        self.img = {}

        #3d dumbells
        self.img["db1"] = load("dumbell_3d_L.png", (230, 230))
        self.img["db2"] = load("dumbell_3d_R.png", (230, 230))

        #navbar images
        NS = (60, 60)
        self.img["home_b"] = load("Nav_home_b.png", NS)
        self.img["home_w"] = load("Nav_home_w.png", NS)
        self.img["log_b"] = load("Nav_log_b.png", NS)
        self.img["log_w"] = load("Nav_log_w.png", NS)
        self.img["workout_w"] = load("Nav_workout_w.png", NS)
        self.img["workout_b"] = load("Nav_workout_b.png", NS)

        #other images
        self.img["stopwatch"] = load("Stopwatch.png", (90,90))
        self.img["scale"] = load("Scale.png", (90,90))

    #Window layout
    def _build_ui(self):
        self.content = tk.Frame(self, bg=BG_LIGHT, width=W, height=H - Nav_H)
        self.content.pack(side="top", fill="both", expand=True)
        nav = tk.Frame(self, bg=BG_NAV, height=Nav_H)
        nav.pack(side="bottom", fill="x")
        nav.pack_propagate(False)









