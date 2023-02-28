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

# PROGRAM END.
