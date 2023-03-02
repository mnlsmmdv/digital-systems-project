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

# Login window frame.
login_window_frame = CTkFrame(login_window_image_label, width=320, height=360, corner_radius=15)
login_window_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Login window header label (login_window_frame).
login_window_header_label = CTkLabel(login_window_frame, text="To continue, log in", font=("SF Pro Display", 20))
login_window_header_label.place(x=75, y=45)

# Login window Username entry (login_window_frame).
login_window_username_entry = CTkEntry(login_window_frame, width=220, placeholder_text='Username')
login_window_username_entry.place(x=50, y=110)

# Login window Password entry (login_window_frame).
login_window_password_entry = CTkEntry(login_window_frame, width=220, placeholder_text='Password', show="*")
login_window_password_entry.place(x=50, y=165)

# Login window Forgot password label (login_window_frame).
login_window_forgot_password_label = CTkLabel(login_window_frame, text="Forget password?", font=("SF Pro Display", 12))
login_window_forgot_password_label.place(x=170, y=195)

# Login window Register button (login_window_frame).
register_button = CTkButton(login_window_frame, text="Register", width=100, corner_radius=6)
register_button.place(x=50, y=240)

# Login window Login button (login_window_frame).
login_button = CTkButton(login_window_frame, text="Login", width=100, corner_radius=6)
login_button.place(x=170, y=240)

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
