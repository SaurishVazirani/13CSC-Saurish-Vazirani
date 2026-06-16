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

