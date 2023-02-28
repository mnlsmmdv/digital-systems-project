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

# List of titles for names according to gender.
title_names = ["", "Mr.", "Mrs.", "Miss.", "Ms.", "Mx.", "Sir.", "Dame.", "Dr.", "Prof.", "Cllr.", "Lady." "Lord."]

# List of numbers 01-100 to select users age.
age_values = [str(i).zfill(2) for i in range(0, 101)]

# List of countries of the United Nations.
country_names_UN = [country.name for country in pycountry.countries]

# PROGRAM END.
