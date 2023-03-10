"""
Name: Ahmed Affaan
Title: registration_window.py
Folder: -
Date: 28/02/2023
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

# List of titles for names according to gender (user_information_frame).
title_names = ["", "Mr.", "Mrs.", "Miss.", "Ms.", "Mx.", "Sir.", "Dame.", "Dr.", "Prof.", "Cllr.", "Lady.", "Lord."]

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
maldives_uk_bank_currencies = [currency.alpha_3 for currency in pycountry.currencies]

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
    # Checks if all required fields have been filled in.
    if (len(first_name_entry.get()) > 0 and len(last_name_entry.get()) > 0 and
            len(name_title_combobox.get()) > 0 and len(user_age_combobox.get()) > 0 and
            len(user_nationality_combobox.get()) > 0 and len(registration_user_name_entry.get()) > 0 and
            len(user_bank_name_combobox.get()) > 0 and len(user_bank_currency_combobox.get()) > 0 and
            terms_conditions_status.get()):
        # Displays success message if all required fields have been filled in.
        CTkMessagebox(title="User Registered", message="Registered successfully!", icon="check", option_1="Ok")
    else:
        # Displays error message if any required fields are missing.
        CTkMessagebox(title="Registration Error", message="Please fill in all required fields!", icon="warning", option_1="Ok")

# This function cancels user registration and goes back to login_window .
def cancel_user_registration():
    # Closes the registration window.
    registration_window.destroy()
    # Opens the login window.
    subprocess.run(["python", "login_window.py"])

# This function displays error popup if user selects age below 18 years old.
def validate_age_combobox(event):
    # Converting string to an integer.
    user_age = int(user_age_combobox.get())

    # Displays error message if selection is less than 18 years old.
    if user_age < 18:
        # Error message.
        CTkMessagebox(title="Unauthorised Selection", message="Must be 18 or higher!", icon="cancel", option_1="Ok")
        user_age_combobox.set("")

# This function displays error popup if user selects country other than Maldives.
def validate_user_nationality_combobox(event):
    # Displays error if selection is not Maldives.
    if user_nationality_combobox.get() != "Maldives":
        # Error message.
        CTkMessagebox(title="Unauthorised Selection", message="Can select Maldives only!", icon="cancel", option_1="Ok")
        user_nationality_combobox.set("")

# This function displays error popup if user selects bank other than Bank of Maldives.
def validate_bank_name_combobox(event):
    # Displays error if selection is not Bank of Maldives.
    if user_bank_name_combobox.get() != "Bank of Maldives":
        # Error message.
        CTkMessagebox(title="Unauthorised Selection", message="Can select Bank of Maldives only!", icon="cancel", option_1="Ok")
        user_bank_name_combobox.set("")

# This function displays error popup if user selects currency other than MVR.
def validate_bank_currency_combobox(event):
    # Displays error if selection is not MVR or USD.
    if user_bank_currency_combobox.get() not in ["USD", "MVR"]:
        # Error message.
        CTkMessagebox(title="Unauthorised Selection", message="Can select MVR or USD only only!", icon="cancel", option_1="Ok")
        user_bank_currency_combobox.set("")

# Registration window configurations.
registration_window = CTk()
registration_window.title("Registration") # Window title.
registration_window.geometry("800x608") # Window dimensions.
#registration_window.resizable(False, False) # Maintaining constant window dimensions.

# Displays background image for registration window.
registration_window_background_image = ImageTk.PhotoImage(Image.open("Images/login_background.jpg"))
registration_window_background_image_label = CTkLabel(registration_window, image=registration_window_background_image)
registration_window_background_image_label.place(x=0, y=0, relwidth=1, relheight=1)

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
user_age_combobox = CTkComboBox(user_information_frame, values=age_values, command=validate_age_combobox)
user_age_combobox.set("")
user_age_combobox.grid(row=3, column=0, padx=10, pady=5)
user_age_combobox.bind("<<ComboboxSelected>>", validate_age_combobox)

# Nationality label and combobox (user_information_frame).
user_nationality_label = CTkLabel(user_information_frame, text="Nationality")
user_nationality_label.grid(row=2, column=1, padx=10, pady=5)
user_nationality_combobox = CTkComboBox(user_information_frame, values=country_names_UN, command=validate_user_nationality_combobox)
user_nationality_combobox.set("")
user_nationality_combobox.grid(row=3, column=1, padx=10, pady=5)
user_nationality_combobox.bind("<<ComboboxSelected>>", validate_user_nationality_combobox)

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

# Bank name label and combobox (bank_information_frame).
user_bank_name_label = CTkLabel(bank_information_frame, text="Bank Name")
user_bank_name_label.grid(row=0, column=1, padx=10, pady=5)
user_bank_name_combobox = CTkComboBox(bank_information_frame, values=maldives_uk_bank_names, command=validate_bank_name_combobox)
user_bank_name_combobox.set("")
user_bank_name_combobox.grid(row=1, column=1, padx=10, pady=5)
user_bank_name_combobox.bind("<<ComboboxSelected>>", validate_bank_name_combobox)

# Bank account currency type and combobox (bank_information_frame).
user_bank_currency_label = CTkLabel(bank_information_frame, text="Currency Type")
user_bank_currency_label.grid(row=0, column=2, padx=10, pady=5)
user_bank_currency_combobox = CTkComboBox(bank_information_frame, values=maldives_uk_bank_currencies, command=validate_bank_currency_combobox)
user_bank_currency_combobox.set("")
user_bank_currency_combobox.grid(row=1, column=2, padx=10, pady=5)
user_bank_currency_combobox.bind("<<ComboboxSelected>>", validate_bank_currency_combobox)

# Frame for Terms and Conditions (T&C).
terms_conditions_frame = CTkFrame(user_registration_frame)
terms_conditions_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)
terms_conditions_frame.columnconfigure(0, weight=1)
terms_conditions_frame.rowconfigure(0, weight=1)

# Terms and conditions text area (terms_conditions_frame).
terms_conditions_text_area = CTkTextbox(terms_conditions_frame, width=75, height=200, wrap="none")
terms_conditions_text_area.insert(END, terms_conditions_text)
terms_conditions_text_area.configure(state=DISABLED)
terms_conditions_text_area.grid(row=1, column=0, sticky="news", padx=10, pady=5)

# Terms and conditions status label and checkbox (terms_conditions_frame).
terms_conditions_status = CTkCheckBox(terms_conditions_frame, text="I accept the terms and conditions")
terms_conditions_status.grid(row=3, column=0, padx=10, pady=5)

# Register user button (user_registration_frame).
register_user_button = CTkButton(user_registration_frame, text="Register User", command=validate_user_registration)
register_user_button.grid(row=3, column=0, padx=10, pady=10)

# Cancel registration button (user_registration_frame).
cancel_registration_button = CTkButton(user_registration_frame, text="Cancel", command=cancel_user_registration)
cancel_registration_button.grid(row=4, column=0, padx=10, pady=10)

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
