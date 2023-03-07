"""
Name: Ahmed Affaan
Title: request_window.py
Folder: -
Date: -
Country: Republic of Maldives
Code version: -
Description: Login window for P2P payment application.
Credits to:
Credits to link: 
Note: Uncomment codes to execute and comment them when not in use.
"""

# PROGRAM START.

# Importing libraries.
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import pycountry
import webbrowser
import os
import subprocess

# Setting general appearence and UI colour theme.
set_appearance_mode("system")
set_default_color_theme("blue")

# Request Window configurations.
global request_window
request_window = CTk()
request_window.title("Request") # Window title.
request_window.geometry("800x608") # Window dimensions.
#request_window.resizable(False, False) # Keeping constant window dimension size.

# Running the main window event loop.
request_window.mainloop()

# PROGRAM END.
