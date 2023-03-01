"""
Name: Ahmed Affaan
Title: login_window.py
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
from customtkinter import *
from CTkMessagebox import CTkMessagebox
import pycountry
import webbrowser
from PIL import ImageTk, Image
import os
from tkinter import filedialog

# Setting general appearence and UI colour theme.
set_appearance_mode("system")
set_default_color_theme("blue")

# Login Window configurations.
global login_window
login_window = CTk()
login_window.title("Login") # Window title.
login_window.geometry("800x608") # Window dimensions.
#login_window.resizable(False, False) # Keeping constant window dimension size.

# Running the main window event loop.
login_window.mainloop()

# PROGRAM END.
