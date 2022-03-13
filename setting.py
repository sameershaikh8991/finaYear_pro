from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from userHandler import UserData
import configparser

background, textColor = 'black', '#F6FAFB'
background, textColor = textColor, background

avatarChoosen = 0
choosedAvtrImage = None
# user = UserData()
# user.extractData()
# UserName = user.getName().split()[0]
# ownerDesignation = "Sir"

def setting():
	root = Tk()
	root.title('JARVIS')
	w_width, w_height = 350, 600
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg=background)

	settingsLbl = Label(root, text='Settings', font=('Arial Bold', 15), bg=background, fg=textColor)
	settingsLbl.pack(pady=10)


	userName = Label(root, text=UserName, font=('Arial Bold', 15), fg=textColor, bg=background)
	userName.pack()
	#Settings Frame
	settingsFrame = Frame(root, width=300, height=300, bg=background)
	settingsFrame.pack(pady=20)

	assLbl = Label(settingsFrame, text='Assistant Voice', font=('Arial', 13), fg=textColor, bg=background)
	assLbl.place(x=0, y=20)
	n = StringVar()
	assVoiceOption = ttk.Combobox(settingsFrame, values=('Female', 'Male'), font=('Arial', 13), width=13, textvariable=n)
	# assVoiceOption.current(voice_id)
	assVoiceOption.place(x=150, y=20)
	# assVoiceOption.bind('<<ComboboxSelected>>', changeVoice)

	usernameCha = Label(settingsFrame, text='Username', font=('Arial', 13), fg=textColor, bg=background)
	usernameCha.place(x=0, y=60)


	PhotoDir = Label(settingsFrame, text='Photo Loc', font=('Arial', 13), fg=textColor, bg=background)
	PhotoDir.place(x=0, y=100)

	Photoinfo = Label(settingsFrame, text='No photo location selected', font=('Arial', 10), fg=textColor, bg=background)
	Photoinfo.place(x=120, y=100)


	SongLoc = Label(settingsFrame, text='SongLoc', font=('Arial', 13), fg=textColor, bg=background)
	SongLoc.place(x=0, y=140)

	Songinfo = Label(settingsFrame, text='no music loc found', font=('Arial', 10), fg=textColor, bg=background)
	Songinfo.place(x=120, y=140)


	Button(root, text='     update    ', bg='#0475BB', fg='white',font=('Arial Bold', 18), bd=0, relief=FLAT,command="").pack(pady=10)
	# n2 = StringVar()
	# voiceOption = ttk.Combobox(settingsFrame, font=('Arial', 13), width=13, textvariable=n2)
	# voiceOption['values'] = ('Very Low', 'Low', 'Normal', 'Fast', 'Very Fast')
	# voiceOption.current(ass_voiceRate//50-2) #100 150 200 250 300
	# voiceOption.place(x=150, y=60)
	# voiceOption.bind('<<ComboboxSelected>>', changeVoiceRate)

	root.iconbitmap('extrafiles/images/assistant2.ico')
	root.mainloop()

