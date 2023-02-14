#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importing necessary libraries
import sys
import tkinter as tk 
import smtplib as sm
from tkinter import ttk

# Variables, used later
saved = False

# Setting up tkInter window
root = tk.Tk()
root.geometry("200x100")
root.resizable(False, False)
root.title("mail")

# window destroying function
def clearWindow(*widgets):
    for widget in widgets:
        # Exits each window defined in *widgets
        widget.destroy

def EmailPrompt():



# Labeling
welcomeLabel = ttk.Label(
    root,
    text="Mail")

detailLabel = ttk.Label(
    root,
    text="Are your details saved?")

yesButton = tk.Button(
    root,
    text="Yes"
    command=lambda: clearWindow(root)
)

