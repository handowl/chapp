from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from TextWidget.TextWidget import *

def exit(args):
	sendMessage(0)
	file.close()
	raise SystemExit()

def checkMessage(text):
	messages = text.rsplit("@text=")
	for msg in messages:
		msg.rsplit("@text=")
		msg.strip(' \t \n \r')

	while "" in messages:
		messages.remove("")
	return messages

def sendMessage(event):
	text = textMessage.get(1.0, END)
	message_s = checkMessage(text)
	for msg in message_s:
		file.write("@text="+msg)
		TextWidget(messFrame, width=40, text=msg.strip(' \n\t\r'), bg="white",  borderwidth=2, relief="solid", font="Arial 13").pack(side="top", ipadx=10, ipady=10, pady=5)
	textMessage.delete(1.0, END)

def main(name, password):
	global pas
	pas = password
	window = Tk()
	window.geometry("800x700")
	window.title(name)
	global textMessage
	textMessage = scrolledtext.ScrolledText(window, font="Arial 13", height=10)
	textMessage.pack(side="bottom")

	global messFrame
	canvas = Canvas(window, bg="blue", height=400)
	messFrame = Frame(canvas,bg="white")
	scroll = Scrollbar(window, orient="vertical", command=canvas.yview)
	canvas.configure(yscrollcommand=scroll.set)
	scroll.pack(side="right", fill="y")
	messFrame.pack(side="top", fill="both", expand="true")
	canvas.pack(side="top", fill="both", expand="true")

	global file 
	file = open(name+".txt", '+r')
	messages = checkMessage(file.read())
	for msg in messages:
		TextWidget(messFrame, width=40, text=msg.strip(' \n\t\r'), bg="white",  borderwidth=2, relief="solid", font="Arial 13").pack(side="top", ipadx=10, ipady=10, pady=5)
	
	canvas.create_window((400,messFrame["height"]*2), window=messFrame, width=800)
	window.bind("<Return>", sendMessage)
	window.bind("<Escape>", exit)
	window.mainloop()
	file.close()

if __name__=="__main__":
	messagebox.showerror("Error!", "You must log in!")
