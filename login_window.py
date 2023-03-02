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

# Login window background image.
login_window_background_image = ImageTk.PhotoImage(Image.open("Images/login_background.jpg"))
login_window_image_label = CTkLabel(login_window, text="Background Image", image=login_window_background_image)
login_window_image_label.pack()

# Configurations to center login window window on initial run.
login_window.update() # Refreshes the window.
login_window_width = login_window.winfo_width() # Retrieves the window width.
login_window_height = login_window.winfo_height() # Retrieves the window height.
screen_width = login_window.winfo_screenwidth() # Retrieves the screen width.
screen_height = login_window.winfo_screenheight() # Retrieves the screen height.
x_axis = int((screen_width / 2) - (login_window_width / 2)) # Calculates x-axis.
y_axis = int((screen_height / 2) - (login_window_height / 2)) # Calculates y-axis.
login_window.geometry(f"{login_window_width}x{login_window_height}+{x_axis}+{y_axis}") # Sets the window size to any screen center.

# Running the main window event loop.
login_window.mainloop()

# PROGRAM END.
