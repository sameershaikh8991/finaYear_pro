from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from userHandler import UserData
# import FACE_UNLOCKER as FU
from cmdlist import *

background, textColor = 'black', '#F6FAFB'
background, textColor = textColor, background

global root2,root2,root3,root4


################################################# GUI ###############################

def Settingpage():
	raise_frame(root2)

def Aboutpage():
	raise_frame(root3)

def Commandpage():
	cmdlist()


def raise_frame(frame):
	frame.tkraise()

if __name__ == '__main__':
# def menu():
	root = Tk()
	root.title('Jarvis')
	w_width, w_height = 350, 600
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg=background)
	# root.resizable(0, 0)
	# root.attributes('-toolwindow', True)
	root1 = Frame(root, bg=background)
	root2 = Frame(root, bg=background)
	root3 = Frame(root, bg=background)

	for f in (root1, root2, root3):
		f.grid(row=0, column=0, sticky='news')	


	detailFrame1 = Frame(root1, bd=10, bg=background)
	detailFrame1.pack(fill=X)
	userFrame1 = Frame(detailFrame1, bd=15, width=300, height=250, relief=FLAT, bg=background)
	userFrame1.pack(padx=10, pady=30)

	settingBtn = Button(userFrame1, text='     Setting    ', bg='#0475BB', fg='white',font=('Arial Bold', 14), bd=0, relief=FLAT,command=Settingpage)
	settingBtn.place(x=90, y=120)
	aboutBtn = Button(userFrame1, text='     About     ', bg='#0475BB', fg='white',font=('Arial Bold', 14), bd=0, relief=FLAT, command=Aboutpage)
	aboutBtn.place(x=90, y=180)
	commandListBtn = Button(detailFrame1, text='     command List     ', bg='#0475BB', fg='white',font=('Arial Bold', 14), bd=0, relief=FLAT, command=Commandpage)
	commandListBtn.place(x=90, y=280)

# 	####################### 	SETTING  PAGE #################

	#Details
	settingFrame = Frame(root2, bd=10, bg=background)
	settingFrame.pack(fill=X)
	settingpageFrame = Frame(settingFrame, bd=15, width=300, height=250, relief=FLAT, bg=background)
	settingpageFrame.pack(padx=10, pady=30)


	backLbl = Button(root2, text='   Back   ', font=('Arial Bold', 10), bg='#01933B', fg='white', command=lambda:raise_frame(root1), relief=FLAT)
	backLbl.place(x=10,y=5)


	#name
	setHead = Label(settingpageFrame, text='Setting', font=('Arial Bold', 18), fg='black', bg=background)
	setHead.place(x=110,y=0)

	nameLbl = Label(settingpageFrame, text='Ai name', font=('Arial Bold', 12), fg='black', bg=background)
	nameLbl.place(x=10,y=40)
	nameField = Entry(settingpageFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
	nameField.focus()
	nameField.place(x=100,y=40)


	genLbl = Label(settingpageFrame, text='Voice', font=('Arial Bold', 12), fg='#303E54', bg=background)
	genLbl.place(x=10,y=85)
	r = IntVar()
	s = ttk.Style()
	s.configure('Wild.TRadiobutton', background=background, foreground=textColor, font=('Arial Bold', 10), focuscolor=s.configure(".")["background"])
	genMale = ttk.Radiobutton(settingpageFrame, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genMale.place(x=80,y=85)
	genFemale = ttk.Radiobutton(settingpageFrame, text='Female', value=2, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genFemale.place(x=150,y=85)

	#add face
	addBtn = Button(settingpageFrame, text='    update    ', font=('Arial Bold', 12), bg='#01933B', fg='white', command="Nextstep", relief=FLAT)
	addBtn.place(x=90, y=200)

	#status of add face
	statusLbl = Label(settingpageFrame, text='', font=('Arial 10'), fg=textColor, bg=background)
	statusLbl.place(x=80, y=190)


	###################### ABOUT PAGE #####################
	AboutFrame = Frame(root3, bd=10, bg=background)
	AboutFrame.pack(fill=X)
	aboutpageFrame = Frame(AboutFrame, bd=15, width=310, height=500, relief=FLAT, bg=background)
	aboutpageFrame.pack(padx=10, pady=30)


	backLbl = Button(root3, text='   Back   ', font=('Arial Bold', 10), bg='#01933B', fg='white', command=lambda:raise_frame(root1), relief=FLAT)
	backLbl.place(x=10,y=5)


	#name
	nameLbl = Label(aboutpageFrame, text='ABOUT', font=('Arial Bold', 18), fg='black', bg=background)
	nameLbl.place(x=100,y=10)

	aboutText ="A virtual assistant is an application that understands voice commands and completes tasks for a user.Virtual assistants like these can do everything from answer questions, tell jokes, play music Virtual assistants learn over time and get to know your habits and preferences, so they're always getting smarter.\n Using artificial intelligence (AI), they understand natural language, recognize faces, identify objects, and communicate with other smart devices and software"

	aboutdata = Label(aboutpageFrame, text=aboutText, font=('Arial Bold', 12),wraplength=280, fg='black', bg=background)
	aboutdata.place(x=10,y=50)

	


	root.iconbitmap('extrafiles/images/aiicon.ico')
	raise_frame(root1)
	root.mainloop()


