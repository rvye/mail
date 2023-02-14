## Python Mail Client
##
## by @rvye

## TODO
##
## Rewrite
import sys
import tkinter as tk
import smtplib as sm
from tkinter import ttk

saved = False
notSaved = False

root = tk.Tk()
root.geometry("200x100")
root.resizable(False, False)
root.title("mail")


def notSavedClear(*widgets):
  for widget in widgets:
    widget.destroy()
  global notSaved
  notSaved = True
def savedClear(*widgets):
  for widget in widgets:
    widget.destroy()
  global saved
  saved = True

# details
welcome = ttk.Label(
  root, 
  text="Mail")
detail_save = ttk.Label(
  root, 
  text="Are your details saved?")
  
# yes / no
ye = tk.Button(
  root, 
  text="Yes", 
  command=lambda: savedClear(root))
nop = tk.Button(
  root, 
  text="No", 
  command=lambda: notSavedClear(root))

## PACKING

welcome.pack(
  padx=30,
  pady=0,)
detail_save.pack(
  padx=10,
  pady=5,)

ye.pack(
  padx=0,
  pady=0,)
nop.pack(
  padx=0,
  pady=0,)

root.mainloop()

###### details prompt ######
if notSaved == True:
  while notSaved == True:
    signin = tk.Tk()
    signin.geometry("300x150")
    signin.resizable(False, False)
    signin.title('Sign In')
  
    def writeToFile():
      email = emailVar.get()
      password = passwordVar.get()
      if email == "":
        sys.exit()
      if password == "":
        sys.exit()
      with open("email.txt", 'w') as e:
        e.seek(0)
        e.write(email)
        e.truncate()
      with open("password.txt", 'w') as p:
        p.seek(0)
        p.write(password)
        p.truncate()
      signin.destroy()
    
    emailVar = tk.StringVar()
    passwordVar = tk.StringVar()
    
    
    # email
    email_label = ttk.Label(signin, text="Email Address:")
    email_entry = ttk.Entry(signin, textvariable=emailVar)
    email_entry.focus()
  
    # password
    password_label = ttk.Label(signin, text="Password:")
    password_entry = ttk.Entry(textvariable=passwordVar, show="*")
  
    # login
    login_button = ttk.Button(signin, text="Login", command=writeToFile)
    
    ## PACKING
    email_label.pack(fill='x', expand=True)
    email_entry.pack(fill='x', expand=True)
    password_label.pack(fill='x', expand=True)
    password_entry.pack(fill='x', expand=True)
    login_button.pack(fill='x', expand=True, pady=10)
    signin.update()
    signin.mainloop()
    send = tk.Tk()
    send.geometry("200x200")
    send.resizable(True, True)
    send.title('Write')

    toVar = tk.StringVar()
    bodyVar = tk.StringVar()
    toLabel = ttk.Label(send, text="Who would you like to send this to?")
    toBox = ttk.Entry(send, textvariable=toVar)
    mailLabel = ttk.Label(send, text="What would you like to say?")
    mail = ttk.Entry(send, textvariable=bodyVar)

    def sendEmail():
      global body
      body = bodyVar.get()
      global to
      to = toVar.get()

      # Opens email.txt
      userr = open("email.txt", 'r')
      user = userr.read()
      userr.close()

      # Opens password.txt
      pw = open("password.txt", 'r')
      password = pw.read()
      pw.close()


      try:
        mail = sm.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()
        mail.login(user,password)
        mail.sendmail(user,to,body)
        mail.quit()
        return 1

      except Exception as ex:
        print("Exception: ", ex)
        return 0

    sendButton = ttk.Button(send, text="Send", command=sendEmail)

    toLabel.pack(fill='x', expand=True)
    toBox.pack(fill='x', expand=True)
    mailLabel.pack(fill='x', expand=True)
    mail.pack(fill='x', expand=True)
    sendButton.pack(fill='x', expand=True)
    send.mainloop()
    send.destroy()

###### sending email ######
if saved == True:
  while saved == True:
    send = tk.Tk()
    send.geometry("200x200")
    send.resizable(True, True)
    send.title('Write')

    toVar = tk.StringVar()
    bodyVar = tk.StringVar()
    toLabel = ttk.Label(send, text="Who would you like to send this to?")
    toBox = ttk.Entry(send, textvariable=toVar)
    mailLabel = ttk.Label(send, text="What would you like to say?")
    mail = ttk.Entry(send, textvariable=bodyVar)


    def sendEmail():
      global body
      body = bodyVar.get()
      global to
      to = toVar.get()

      # Opens email.txt
      userr = open("email.txt", 'r')
      user = userr.read()
      userr.close()

      # Opens password.txt
      pw = open("password.txt", 'r')
      password = pw.read()
      pw.close()

      try:
        mail = sm.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.ehlo()
        mail.login(user,password)
        mail.sendmail(user,to,body)
        mail.quit()
        return 1

      except Exception as ex:
        print("Exception: ", ex)
        return 0

    sendButton = ttk.Button(send, text="Send", command=sendEmail)

    toLabel.pack(fill='x', expand=True)
    toBox.pack(fill='x', expand=True)
    mailLabel.pack(fill='x', expand=True)
    mail.pack(fill='x', expand=True)
    sendButton.pack(fill='x', expand=True)
    send.mainloop()
    send.destroy()
