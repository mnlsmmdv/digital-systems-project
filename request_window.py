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

# Request window background image.
request_window_background_image = ImageTk.PhotoImage(Image.open("Images/login_background.jpg"))
request_window_image_label = CTkLabel(request_window, text="Background Image", image=request_window_background_image)
request_window_image_label.pack()

# Request window frame.
request_window_frame = CTkFrame(request_window_image_label, width=320, height=330, corner_radius=15)
request_window_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Request window header label (request_window_frame).
login_window_header_label = CTkLabel(request_window_frame, text="Request, pending payment", font=("SF Pro Display", 20))
login_window_header_label.place(x=38, y=45)

# Request window entry (request_window_frame).
request_window_username_entry = CTkEntry(request_window_frame, width=220)
request_window_username_entry.place(x=50, y=100)

# Configurations to center request_window on initial run.
request_window.update() # Refreshes the window.
request_window_width = request_window.winfo_width() # Retrieves the window width.
request_window_height = request_window.winfo_height() # Retrieves the window height.
screen_width = request_window.winfo_screenwidth() # Retrieves the screen width.
screen_height = request_window.winfo_screenheight() # Retrieves the screen height.
x_axis = int((screen_width / 2) - (request_window_width / 2)) # Calculates x-axis.
y_axis = int((screen_height / 2) - (request_window_height / 2)) # Calculates y-axis.
request_window.geometry(f"{request_window_width}x{request_window_height}+{x_axis}+{y_axis}") # Sets the window size to any screen center.

# Running the main window event loop.
request_window.mainloop()

# PROGRAM END.
