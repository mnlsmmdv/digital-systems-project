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

# This function displays an error if user enters invalid values and clicks the "Add Msg" button.
def display_error_add_message_button():
    # Placeholder.
    pass

# This function cancels user request and goes back to overview_window .
def cancel_user_request():
    # Closes the request_window .
    request_window.destroy()
    # Opens the overview_window .
    subprocess.run(["python", "overview_window.py"])

# This function will display the message variable values.
def update_request_entry(input_value):
    display_message = request_entry_message.get()
    request_entry_message.set(display_message + input_value)

# This function validates request amount is not greather than application limit.
def validate_request_amount():
    # Retrieves amount entered by from the entry field.
    request_amount = request_entry_message.get()

    # Displays error popup if entry is empty and request button is clicked.
    if not request_amount:
        # Error message.
        CTkMessagebox(title="Unauthorised Action", message="Please enter amount!", icon="cancel", option_1="Ok")
        return
    
    # Converting request amount to float value.
    try:
        request_amount_float = float(request_amount)
        # Displays error popup if request amount is greater than 5000 and clears entry.
        if request_amount_float > 5000:
            CTkMessagebox(title="Unauthorised Amount", message="Amount can not exceed 5000!", icon="cancel", option_1="Ok")
            request_entry_message.set("")
        # Displays no error if request amount is not greather than 5000.
        else:
            pass
    # Displays error popup if float amount conversion fails.
    except ValueError:
        # Error message.
        CTkMessagebox(title="Unauthorised Amount", message="Must be a valid amount!", icon="cancel", option_1="Ok")
        request_entry_message.set("")

# This function clears the message entry field.
def clear_request_entry():
    # Clears the entry.
    request_entry_message.set("")

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
request_window_frame = CTkFrame(request_window_image_label, width=320, height=350, corner_radius=15)
request_window_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Stores entry message.
request_entry_message = StringVar()

# Request window header label (request_window_frame).
request_window_header_label = CTkLabel(request_window_frame, text="Request, pending payment", font=("SF Pro Display", 20))
request_window_header_label.place(x=38, y=45)

# Request window entry (request_window_frame).
request_window_message_entry = CTkEntry(request_window_frame, border_color="", width=220, textvariable=request_entry_message)
request_window_message_entry.place(x=50, y=100)

# Request window buttons (request_window_frame).
button_one = CTkButton(request_window_frame, text="1", width=70, corner_radius=6, command=lambda: update_request_entry("1")) # Button one.
button_one.place(x=50, y=150)
button_two = CTkButton(request_window_frame, text="2", width=70, corner_radius=6, command=lambda: update_request_entry("2")) # Button two.
button_two.place(x=125, y=150)
button_three = CTkButton(request_window_frame, text="3", width=70, corner_radius=6, command=lambda: update_request_entry("3")) # Button three.
button_three.place(x=200, y=150)
button_four = CTkButton(request_window_frame, text="4", width=70, corner_radius=6, command=lambda: update_request_entry("4")) # Button four.
button_four.place(x=50, y=185)
button_five = CTkButton(request_window_frame, text="5", width=70, corner_radius=6, command=lambda: update_request_entry("5")) # Button five.
button_five.place(x=125, y=185)
button_six = CTkButton(request_window_frame, text="6", width=70, corner_radius=6, command=lambda: update_request_entry("6")) # Button six.
button_six.place(x=200, y=185)
button_seven = CTkButton(request_window_frame, text="7", width=70, corner_radius=6, command=lambda: update_request_entry("7")) # Button seven.
button_seven.place(x=50, y=220)
button_eight = CTkButton(request_window_frame, text="8", width=70, corner_radius=6, command=lambda: update_request_entry("8")) # Button eight.
button_eight.place(x=125, y=220)
button_nine = CTkButton(request_window_frame, text="9", width=70, corner_radius=6, command=lambda: update_request_entry("9")) # Button nine.
button_nine.place(x=200, y=220)
request_button = CTkButton(request_window_frame, text="Request", width=70, corner_radius=6) # Request button.
request_button.place(x=50, y=255)
button_zero = CTkButton(request_window_frame, text="0", width=70, corner_radius=6, command=lambda: update_request_entry("0")) # Button zero.
button_zero.place(x=125, y=255)
cancel_button = CTkButton(request_window_frame, text="Cancel", width=70, corner_radius=6, command=cancel_user_request) # Cancel button.
cancel_button.place(x=200, y=255)
add_message_button = CTkButton(request_window_frame, text="Add Msg", width=70, corner_radius=6) # Add Message button.
add_message_button.place(x=50, y=290)
button_decimal = CTkButton(request_window_frame, text=".", width=70, corner_radius=6, command=lambda: update_request_entry(".")) # Decimal button.
button_decimal.place(x=125, y=290)
clear_button = CTkButton(request_window_frame, text="Clear", width=70, corner_radius=6, command=clear_request_entry) # Clear button.
clear_button.place(x=200, y=290)

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
