"""
Name: Ahmed Affaan
Title: registration_window.py
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
import os
import subprocess

# List of titles for names according to gender (user_information_frame).
title_names = ["", "Mr.", "Mrs.", "Miss.", "Ms.", "Mx.", "Sir.", "Dame.", "Dr.", "Prof.", "Cllr.", "Lady." "Lord."]

# List of numbers 01-100 to select users age (user_information_frame).
age_values = [str(i).zfill(2) for i in range(0, 101)]

# List of countries of the United Nations (user_information_frame).
country_names_UN = [country.name for country in pycountry.countries]

# List of banks operating in the Maldives and some of in the UK.
maldives_uk_bank_names = [
    "", "Bank of Maldives", "Maldives Islamic Bank", "State Bank of India",
    "Habib Bank Limited", "MCB Bank Limited", "Islamic Development Bank", 
    "Abu Dhabi Islamic Bank", "HDFC Bank", "HSBC Bank", "Barclays Bank",
    "Lloyds Bank", "NatWest Bank", "Santander UK", "Nationwide Building Society",
    "TSB Bank", "Royal Bank of Scotland (RBS)", "Halifax", "Bank of Scotland"
]

# List of currencies worldwide.
maldives__bank_currencies = [currency.alpha_3 for currency in pycountry.currencies]

# Terms and Conditions (T & C) text for the text area.
terms_conditions_text = """MIT License

Copyright (c) 2023 Ahmed Affaan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# This function checks all fields have been filled.
def validate_user_registration():
    # Placeholder.
    pass

# This function cancels user registration and goes back to login_window .
def cancel_user_registration():
    # Placeholder.
    pass

# This function displays error popup if user selects age below 18 years old.
def validate_age_combobox():
    # Placeholder.
    pass

# This function displays error popup if user selects country other than Maldives.
def validate_user_nationality_combobox():
    # Placeholder.
    pass

# This function displays error popup if user selects bank other than Bank of Maldives.
def validate_bank_name_combobox():
    # Placeholder.
    pass

# This function displays error popup if user selects currency other than MVR.
def validate_bank_currency_combobox():
    # Placeholder.
    pass

# Registration window configurations.
registration_window = CTk()
registration_window.title("Registration") # Window title.
registration_window.geometry("800x608") # Window dimensions.
#registration_window.resizable(False, False) # Maintaining constant window dimensions.

# Registration window frame configurations.
user_registration_frame = CTkFrame(registration_window)
user_registration_frame.pack(pady=60)

# Frame for saving user information.
user_information_frame = CTkFrame(user_registration_frame)
user_information_frame.grid(row=0, column=0, sticky="news", padx=20, pady=20)

# First Name label and entry (user_information_frame).
first_name_label = CTkLabel(user_information_frame, text="First Name")
first_name_label.grid(row=0, column=0)
first_name_entry = CTkEntry(user_information_frame)
first_name_entry.grid(row=1, column=0, padx=10, pady=5)

# Last Name label and entry (user_information_frame).
last_name_label = CTkLabel(user_information_frame, text="Last Name")
last_name_label.grid(row=0, column=1)
last_name_entry = CTkEntry(user_information_frame)
last_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Title label and combobox (user_information_frame).
name_title = CTkLabel(user_information_frame, text="Title")
name_title.grid(row=0, column=2, padx=10, pady=5)
name_title_combobox = CTkComboBox(user_information_frame, values=title_names)
name_title_combobox.set("")
name_title_combobox.grid(row=1, column=2, padx=10, pady=5)

# Age label and combobox (user_information_frame).
user_age_label = CTkLabel(user_information_frame, text="Age")
user_age_label.grid(row=2, column=0, padx=10, pady=5)
user_age_combobox = CTkComboBox(user_information_frame, values=age_values)
user_age_combobox.set("")
user_age_combobox.grid(row=3, column=0, padx=10, pady=5)

# Nationality label and combobox (user_information_frame).
user_nationality_label = CTkLabel(user_information_frame, text="Nationality")
user_nationality_label.grid(row=2, column=1, padx=10, pady=5)
user_nationality_combobox = CTkComboBox(user_information_frame, values=country_names_UN)
user_nationality_combobox.set("")
user_nationality_combobox.grid(row=3, column=1, padx=10, pady=5)

# Username label and entry (user_information_frame).
registration_user_name_label = CTkLabel(user_information_frame, text="Username")
registration_user_name_label.grid(row=2, column=2, padx=10, pady=5)
registration_user_name_entry = CTkEntry(user_information_frame)
registration_user_name_entry.grid(row=3, column=2, padx=10, pady=5)

# Frame for saving user bank information.
bank_information_frame = CTkFrame(user_registration_frame)
bank_information_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Bank account status label and checkbox (bank_information_frame).
user_bank_status_label = CTkLabel(bank_information_frame, text="Account Status")
user_bank_status_label.grid(row=0, column=0, padx=10, pady=5)
user_bank_status_checkbox = CTkCheckBox(bank_information_frame, text="Account Active")
user_bank_status_checkbox.grid(row=1, column=0, padx=10, pady=5)

# Configurations to center registration window on initial run.
registration_window.update() # Refreshes the window.
registration_window_width = registration_window.winfo_width() # Retrieves the window width.
registration_window_height = registration_window.winfo_height() # Retrieves the window height.
screen_width = registration_window.winfo_screenwidth() # Retrieves the screen width.
screen_height = registration_window.winfo_screenheight() # Retrieves the screen height.
x_axis = int((screen_width / 2) - (registration_window_width / 2)) # Calculates x-axis.
y_axis = int((screen_height / 2) - (registration_window_height / 2)) # Calculates y-axis.
registration_window.geometry(f"{registration_window_width}x{registration_window_height}+{x_axis}+{y_axis}") # Sets the window size to any screen center.

# Running the registration_window event loop.
registration_window.mainloop()

# PROGRAM END.
