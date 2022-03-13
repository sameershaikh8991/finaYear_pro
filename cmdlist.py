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

background="white"


def cmdlist():
	root = Tk()
	root.title('Command list')
	w_width, w_height = 500, 600
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg=background)
	root.resizable(0, 0)
	# root.attributes('-toolwindow', 1)
	# root.attributes('-alpha', 0.5)
	# root.iconify()

	nameLbl = Label(root, text=' COMMAND LIST  ', font=('Arial Bold', 18), fg='black', bg=background)
	nameLbl.place(x=150,y=10)

	keyword = Label(root, text=' keyword  ', font=('Arial Bold', 18), fg='black', bg=background)
	keyword.place(x=50,y=50)


	task = Label(root, text=' Task  ', font=('Arial Bold', 18), fg='black', bg=background)
	task.place(x=350,y=50)


	task1 = Label(root, text='open google/google		open google', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=100)

	task1 = Label(root, text='open YouTube/youtube		open Youtube', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=135)

	task1 = Label(root, text='take screenshot/screensh		open google', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=170)

	task1 = Label(root, text='send email/email/mail		to send mail', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=205)


	task1 = Label(root, text='goodbye/exit 			    to stop ai', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=240)

	task1 = Label(root, text='open google/google		open google', font=('Arial Bold', 12), fg='black', bg=background)
	task1.place(x=30,y=275)


	root.iconbitmap('extrafiles/images/list.ico')
	# raise_frame(root1)
	root.mainloop()

