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

"""""
This is only called if the user clicks yes when asked
if their details are saved
"""""
# The window used for actually sending the email
def EmailPrompt():
    # Destroying the original window, so there isn't 2 windows open at the same time
    clearWindow(root)

    # Setting up tkInter windows
    prompt = tk.Tk()
    prompt.geometry("200x200")
    prompt.resizable(True, True)
    prompt.title("Send your Email")
    """""""""
    Setting up the variables
    used when sending the email
    aswell as labeling them
    """""""""
    # To variables
    toInput = tk.StringVar()
    toLabel = ttk.Label(prompt, text="Who would you like to send this to?")
    toBox = ttk.Entry(prompt, textvariable=toInput)

    # Body variables
    bodyInput = tk.StringVar
    bodyLabel = ttk.Label(prompt, text="What would you like to say?")
    bodyBox = ttk.Label(prompt, textvariable=bodyInput)

    # Function used for actually sending the email
    def sendEmail():
        """""
        # Actually getting the inputted text
        # from toBox, and bodyBox, so that the 
        # email will be properly sent.
        """""
        to = toBox.get()
        body = bodyBox.get()
        
        # Opens the file containing user login
        userFile = open("email.txt", "r")
        user = userFile.read()
        userFile.close()

        # Opens the file containing user password
        passFile = open("pass.txt", "r")
        pass = passFile.read()
        userFile.close()
        
        # Sending the email
        try:
            mail = sm.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.ehlo()

            # Logging into the SMTP Server
            mail.login(user, pass)

            # Actually sending the email
            mail.sendmail(user, to, body)
            mail.quit()
            return 1

        except exepction as ex:
            print("Exception: ", ex)
            return 0

    # Button for sending the email
    send = ttk.Button(prompt, text = "Send", command = lambda:sendEmail())

    # Packing the Labels, Prompts, and Buttons, allowing them to display onscreen
    
    # Packing the "to" boxes and labels
    toBox.pack(fill='x', expand=True)
    toLabel.pack(fill='x', expand=True)

    # Packing the "body" boxes and labels
    bodyBox.pack(fill='x', expand=True)
    bodyLabel.pack(fill='x', expand=True)

    # Packing the send Button
    send.pack(fill='x', expand=True)

    # Exiting, and watching for any changes
    prompt.mainloop()
    clearWindow(prompt)


# Used for saving user login info
def EmailPrompt():
    clearWindow(root)








# Labeling
welcomeLabel = ttk.Label(
    root,
    text="Mail")

detailLabel = ttk.Label(
    root,
    text="Are your details saved?")


# User input, used for asking if the user's details are saved
yesButton = tk.Button(
    root,
    text="Yes"
    command=lambda: EmailPrompt())

noButton = tk.Button(
    root,
    text="No",
    command=lambda: LoginPrompt())

