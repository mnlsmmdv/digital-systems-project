"""
Name: Ahmed Affaan
Title: overview_window.py
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

# Overview Window configurations.
global overview_window
overview_window = CTk()
overview_window.title("Overview") # Window title.
overview_window.geometry("800x608") # Window dimensions.
#overview_window.resizable(False, False) # Keeping constant window dimension size.

# Overview window background image.
overview_window_background_image = ImageTk.PhotoImage(Image.open("Images/login_background.jpg"))
overview_window_image_label = CTkLabel(overview_window, text="Background Image", image=overview_window_background_image)
overview_window_image_label.pack()

# Overview window frame.
overview_window_frame = CTkFrame(overview_window_image_label, width=900, height=700, corner_radius=15)
overview_window_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Configurations to center overview_window on initial run.
overview_window.update() # Refreshes the window.
overview_window_width = overview_window.winfo_width() # Retrieves the window width.
overview_window_height = overview_window.winfo_height() # Retrieves the window height.
screen_width = overview_window.winfo_screenwidth() # Retrieves the screen width.
screen_height = overview_window.winfo_screenheight() # Retrieves the screen height.
x_axis = int((screen_width / 2) - (overview_window_width / 2)) # Calculates x-axis.
y_axis = int((screen_height / 2) - (overview_window_height / 2)) # Calculates y-axis.
overview_window.geometry(f"{overview_window_width}x{overview_window_height}+{x_axis}+{y_axis}") # Sets the window size to any screen center.

# Running the main window event loop.
overview_window.mainloop()

# PROGRAM END.
