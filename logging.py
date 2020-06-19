from tkinter import *
from tkinter import messagebox
import main
import configparser

def load():
	config = configparser.ConfigParser()
	config.read('settings.ini')
	textLogin.set(config['DEFAULT']['UserName'])
	if config['DEFAULT']['UserName'] == '': check.set(0)
	else: check.set(1)
	
def save():
	config = configparser.ConfigParser()
	if check.get()==1:
		config['DEFAULT'] = {'UserName':textLogin.get()}
	else: config['DEFAULT']['UserName'] = ''
	with open('settings.ini', 'w') as file:
		config.write(file)

def enter(event):
	if textLogin.get() == "":
		messagebox.showerror("Error!", "You must enter the login!")
	else:
		save()
		loggWindow.destroy()
		main.main(textLogin.get(), textPassword.get())

def exit(self):
	save()
	raise SystemExit

loggWindow = Tk()
loggWindow.geometry("400x300")
loggWindow.title("Enter")
textLogin = StringVar()
textPassword = StringVar()
check = IntVar()
check.set(1)
load()
Entry(font="Arial 20", justify='center', textvariable=textLogin).pack(side='top',pady=40, ipady=3)
Entry(font="Arial 20", show="*", justify='center', textvariable=textPassword).pack(side='top', ipady=3)
Checkbutton(text="Save login",  variable=check).pack()
Button(width=10, font="Arial 15", text="Enter", command=enter).pack(side='top', pady=40)

loggWindow.bind("<Escape>", exit)
loggWindow.bind("<Return>", enter)

loggWindow.mainloop()
