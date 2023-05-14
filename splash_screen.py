"""
Name: Ahmed Affaan
Title: splash_screen.py
Folder: -
Date: -
Country: Republic of Maldives
Code version: -
Description: Login window for P2P payment application.
Note: Uncomment codes to execute and comment them when not in use.
"""

# PROGRAM START.

# Importing libraries.
from tkinter import *
from tkinter import messagebox
import webbrowser
import os

# This function displays about information box.
def menubar_about_box():
    messagebox.showinfo(title="Project Alpha", message="Version:\nCommit:\nDate: 2022-11-03\nPython: 03.10.17\nOS: Windows_NT x64 10.0.22621\nSandboxed: No")

# This function opens the login window.
def open_login_window():
    os.system('python login_window.py')

# Splash screen window configurations.
splash_screen = Tk()
splash_screen.title("Project Alpha") # Window title.
splash_screen.geometry("800x608") # Window dimensions.
splash_screen.resizable(False, False) # Keeping constant window dimension size.
splash_screen.configure(bg="#191414")

# Splash screen menu bar and options.
splash_screen_menubar = Menu(splash_screen)
splash_screen.config(menu=splash_screen_menubar)
splash_screen_menuFile = Menu(splash_screen_menubar, tearoff=0) # File menu.
splash_screen_menubar.add_cascade(label="File", menu=splash_screen_menuFile)
splash_screen_menuFile.add_command(label="Add New Login")
splash_screen_menuFile.add_command(label="Add New Item")
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Sync Wallet")
splash_screen_menuFile.add_command(label="Export Wallet")
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Sync Wallet")
splash_screen_menuFile.add_command(label="Lock Wallet")
splash_screen_menuFile.add_command(label="Log Out", command=quit)
splash_screen_menuFile.add_separator()
splash_screen_menuFile.add_command(label="Quit Project Alpha", command=quit)
splash_screen_menuEdit = Menu(splash_screen_menubar, tearoff=0) # Edit menu.
splash_screen_menubar.add_cascade(label="Edit", menu=splash_screen_menuEdit)
splash_screen_menuEdit.add_command(label="Undo")
splash_screen_menuEdit.add_command(label="Redo")
splash_screen_menuEdit.add_separator()
splash_screen_menuEdit.add_command(label="Cut")
splash_screen_menuEdit.add_command(label="Copy")
splash_screen_menuEdit.add_command(label="Paste")
splash_screen_menuEdit.add_separator()
splash_screen_menuEdit.add_command(label="Copy Username")
splash_screen_menuEdit.add_command(label="Copy Password")
splash_screen_menuEdit.add_command(label="Copy Verification Code (TOTP)")
splash_screen_menuView = Menu(splash_screen_menubar, tearoff=0) # View menu.
splash_screen_menubar.add_cascade(label="View", menu=splash_screen_menuView)
splash_screen_menuView.add_command(label="Zoom In")
splash_screen_menuView.add_command(label="Zoom Out")
splash_screen_menuView.add_command(label="Reset Zoom")
splash_screen_menuView.add_separator()
splash_screen_menuView.add_command(label="Toggle Full Screen")
splash_screen_menuView.add_separator()
splash_screen_menuView.add_command(label="Reload")
splash_screen_menuView.add_command(label="Toggle Developer Tools")
splash_screen_menuAccount = Menu(splash_screen_menubar, tearoff=0) # Account menu.
splash_screen_menubar.add_cascade(label="Account", menu=splash_screen_menuAccount)
splash_screen_menuAccount.add_command(label="Premium Membership")
splash_screen_menuAccount.add_command(label="Change Password")
splash_screen_menuAccount.add_command(label="Two-Step Login")
splash_screen_menuAccount.add_command(label="Secure Phrase")
splash_screen_menuAccount.add_separator()
splash_screen_menuAccount.add_command(label="Delete Account")
splash_screen_menuWindow = Menu(splash_screen_menubar, tearoff=0) # Window menu.
splash_screen_menubar.add_cascade(label="Window", menu=splash_screen_menuWindow)
splash_screen_menuWindow.add_command(label="Minimize")
splash_screen_menuWindow.add_command(label="Hide to Tray")
splash_screen_menuWindow.add_command(label="Maximize")
splash_screen_menuWindow.add_separator()
splash_screen_menuWindow.add_command(label="Close", command=quit)
splash_screen_menuHelp = Menu(splash_screen_menubar, tearoff=0) # Help menu.
splash_screen_menubar.add_cascade(label="Help", menu=splash_screen_menuHelp)
splash_screen_menuHelp.add_command(label="Get Help")
splash_screen_menuHelp.add_command(label="Contact Us")
splash_screen_menuHelp.add_command(label="File a Bug Report")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Follow Us")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Go to Website", command=lambda:webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Get Mobile App")
splash_screen_menuHelp.add_command(label="Get Browser Extension")
splash_screen_menuHelp.add_separator()
splash_screen_menuHelp.add_command(label="Check for Updates...")
splash_screen_menuHelp.add_command(label="About Project Alpha", command=menubar_about_box)

# Splash screen labels.
splash_screen_label1 = Label(splash_screen, text="Project Alpha", font=("consolas bold", 20), bg="#191414", fg="#FFFFFF")
splash_screen_label1.pack()
splash_screen_label1.place(x=300, y=255) # Label placement.
splash_screen_label2 = Label(splash_screen, text="Welcome to the official Project Alpha app\nIt's fast and secure", font=("consolas", 11), bg="#191414", fg="#555555")
splash_screen_label2.pack()
splash_screen_label2.place(x=235, y=320) # Label placement.

# Configurations to center splash screen window on initial run.
splash_screen.update() # Refreshes the window.
splash_screen_width = splash_screen.winfo_width() # Retrieves the window width.
splash_screen_height = splash_screen.winfo_height() # Retrieves the window height.
screen_width = splash_screen.winfo_screenwidth() # Retrieves the screen width.
screen_height = splash_screen.winfo_screenheight() # Retrieves the screen height.
x = int((screen_width / 2) - (splash_screen_width / 2)) # Calculates x-axis.
y = int((screen_height / 2) - (splash_screen_height / 2)) # Calculates y-axis.
splash_screen.geometry(f"{splash_screen_width}x{splash_screen_height}+{x}+{y}") # Sets the window size to any screen center.
splash_screen_button1 = Button(splash_screen, text="START REQUESTING", font=("consolas bold", 11), bg="#1DB954", fg="#FFFFFF", width=5, height=2, command=open_login_window) # Button for splash screen.
splash_screen_button1.place(x=335, y=410, width=145) # Button placement.

# Loops all windows.
splash_screen.mainloop()

# PROGRAM END.
