import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
import threading
import time

#colours
BG_LIGHT = "#7EB5E8"
BG_NAV   = "#3B5BDB"
BG_CARD  = "#3B5BDB"
BTN_DARK = "#111111"
TEXT_W   = "#ffffff"
TEXT_D   = "#111111"

W, H  = 1150, 720
NAV_H = 90

# routines
ROUTINES = {
    "PUSH / PULL / LEGS": [
        {"name": "Bench Press",        "sets": [{"kg": "60", "reps": "8"}, {"kg": "60", "reps": "8"}, {"kg": "60", "reps": "8"}]},
        {"name": "Overhead Press",     "sets": [{"kg": "40", "reps": "8"}, {"kg": "40", "reps": "8"}, {"kg": "40", "reps": "8"}]},
        {"name": "Incline Dumbbell Press", "sets": [{"kg": "24", "reps": "10"}, {"kg": "24", "reps": "10"}, {"kg": "24", "reps": "10"}]},
        {"name": "Tricep Pushdown",    "sets": [{"kg": "20", "reps": "12"}, {"kg": "20", "reps": "12"}, {"kg": "20", "reps": "12"}]},
        {"name": "Lateral Raises",     "sets": [{"kg": "10", "reps": "15"}, {"kg": "10", "reps": "15"}, {"kg": "10", "reps": "15"}]},
    ],
    "UPPER / LOWER": [
        {"name": "Barbell Row",        "sets": [{"kg": "60", "reps": "8"}, {"kg": "60", "reps": "8"}, {"kg": "60", "reps": "8"}]},
        {"name": "Pull Ups",           "sets": [{"kg": "BW", "reps": "8"}, {"kg": "BW", "reps": "8"}, {"kg": "BW", "reps": "8"}]},
        {"name": "Barbell Curl",       "sets": [{"kg": "30", "reps": "10"}, {"kg": "30", "reps": "10"}, {"kg": "30", "reps": "10"}]},
        {"name": "Face Pulls",         "sets": [{"kg": "15", "reps": "15"}, {"kg": "15", "reps": "15"}, {"kg": "15", "reps": "15"}]},
    ],
    "FULL BODY": [
        {"name": "Squat",              "sets": [{"kg": "80", "reps": "5"}, {"kg": "80", "reps": "5"}, {"kg": "80", "reps": "5"}]},
        {"name": "Romanian Deadlift",  "sets": [{"kg": "70", "reps": "8"}, {"kg": "70", "reps": "8"}, {"kg": "70", "reps": "8"}]},
        {"name": "Leg Press",          "sets": [{"kg": "120", "reps": "10"}, {"kg": "120", "reps": "10"}, {"kg": "120", "reps": "10"}]},
        {"name": "Leg Curl",           "sets": [{"kg": "40", "reps": "12"}, {"kg": "40", "reps": "12"}, {"kg": "40", "reps": "12"}]},
        {"name": "Calf Raises",        "sets": [{"kg": "50", "reps": "15"}, {"kg": "50", "reps": "15"}, {"kg": "50", "reps": "15"}]},
    ],
}

def hover(widget, on_col, off_col):
    widget.bind("<Enter>", lambda e: widget.config(bg=on_col))
    widget.bind("<Leave>", lambda e: widget.config(bg=off_col))


class RepFit(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("RepFit – Progress, Not Perfection")
        self.geometry(f"{W}x{H}")
        self.resizable(False, False)
        self.configure(bg=BG_LIGHT)

        self.log: list[dict] = []
        self._timer_secs    = 0
        self._timer_running = False

        self._build_nav()
        self.show_home()

#NavBar
def _build_nav(self):
    self.nav = tk.Frame(self, bg=BG_NAV, height=NAV_H)
    self.nav.pack(side="bottom", fill="x")
    self.nav.pack_propagate(False)
    self._nav_btns = {}
    for i, (label, key, cmd) in enumerate([
        ("Home", "home", self.show_home),
        ("Workouts", "workouts", self.show_workouts),
        ("Logs", "logs", self.show_logs),
    ]):
        self.nav.columnconfigure(i, weight=1)
        btn = tk.Label(self.nav, text=label, bg=BG_NAV, fg=TEXT_W, font=("Arial", 15, "bold"), cursor="hand2", pady=18)
        btn.grid(row=0, column=i, sticky="nsew")
        btn.bind("<Button-1>", lambda e, c=cmd: c())
        hover(btn, "#4a6ae8", BG_NAV)
        self._nav_btns[key] = btn

