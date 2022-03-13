from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from os.path import isfile, join
from threading import Thread
from userHandler import UserData
from time import sleep
from playsound import playsound
import pygame
# import FACE_UNLOCKER as FU

background, textColor = 'black', '#F6FAFB'
background, textColor = textColor, background

avatarChoosen = 0
choosedAvtrImage = None
user_name = ''
user_gender = ''
password = ''
buttonbgcolor = "#013c68"


if os.path.exists('userData')==False:
	os.mkdir('userData')

def Nextstep():

	global user_name, password, user_gender
	user_name = nameField.get()
	password = passwordField.get()
	
	user_gender = r.get()
	if user_name != '' and user_gender!=0 and password!='':
		if agr.get()==1:
			gen = 'Male'
			if user_gender==2: gen = 'Female'
			u = UserData()
			u.updateData(user_name ,password,gen)
			usernameLbl['text'] = user_name
			raise_frame(root4)
			# raise_frame(root3)
		else:
			statusLbl['text'] = '(Check the Condition)'
	else:
		statusLbl['text'] = '(Please fill the details)'


def SuccessfullyRegistered():
	if avatarChoosen != 0:
		gen = 'Male'
		if user_gender==2: gen = 'Female'
		u = UserData()
		u.updateData(user_name ,password,gen, avatarChoosen)
		usernameLbl['text'] = user_name
		raise_frame(root4)

def Registerpage():
	raise_frame(root2)


def Loginpage():
	raise_frame(root5)

def Backbtn():
	raise_frame(root1)

def forgotpassword():
	print("enter in loop")
	logUserName = loginnameField1.get()
	try:
		if logUserName !='':
			user = UserData()
			user.extractData()
			userName = user.getName().split()[0]
			password = user.getPass().split()[0]
			if logUserName == userName:
				print(password)
				showpassword['text'] = password
			else:
				# print("username or password wronge")
				showpasserror['text'] = 'wronge username'
		else:
			# print("plz fill")
			showpasserror['text'] = 'please filled the username'

	except Exception as e:
		print(e)



def LoginCheck():
	logUserName = loginnameField.get()
	loginPassword = loginpasswordField.get()
	# print("username",userName)
	# print("password",password)
	try:
		if logUserName !='' and loginPassword !='':
			user = UserData()
			user.extractData()
			userName = user.getName().split()[0]
			password = user.getPass().split()[0]
			if logUserName == userName and loginPassword ==password:
				root.destroy()
				os.system('python main.py')
			else:
				# print("username or password wronge")
				loginErrorLbl['text'] = 'username or password wronge'
		else:
			# print("plz fill")
			loginErrorLbl['text'] = 'please filled the username or password'

	except Exception as e:
		print(e)


################################################# GUI ###############################


def raise_frame(frame):
	frame.tkraise()

pygame.mixer.init()
if __name__ == '__main__':
	root = Tk()
	root.title('Mark')
	# playsound('extrafiles/audio/intro.mp3')
	pygame.mixer.music.load("extrafiles/audio/intro.mp3")
	pygame.mixer.music.play(loops=0)
	# s = ttk.Style()
	# s.theme_use('alt')
	w_width, w_height = 450, 300
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg=background)
	# root.attributes('-toolwindow', True)
	root.resizable(0, 0)
	root1 = Frame(root, bg=background)
	root2 = Frame(root, bg=background)
	root3 = Frame(root, bg=background)
	root4 = Frame(root, bg=background)
	root5 = Frame(root, bg=background)
	root6 = Frame(root, bg=background)

	for f in (root1, root2, root3, root4,root5,root6):
		f.grid(row=0, column=0, sticky='news')	


	#welcome label
	welcLbl = Label(root1, text='Hi there,\nWelcome to the virtual\n persnoal assistant', font=('Arial Bold', 15), fg='black', bg=background)
	welcLbl.pack(padx=130, pady=20)

	regBtn = Button(root1, text='     Register    ', bg=buttonbgcolor, fg='#ffecd1',font=('Arial Bold', 15), bd=0, relief=FLAT,command=Registerpage)
	regBtn.place(x = 30,y=150)
	logBtn = Button(root1, text='     Login     ', bg=buttonbgcolor, fg='#ffecd1',font=('Arial Bold', 15), bd=0, relief=FLAT, command=Loginpage)
	logBtn.place(x =290, y=150)

	detailFrame2 = Frame(root2, bd=10, bg=background)
	detailFrame2.pack(fill=X)
	userFrame2 = Frame(detailFrame2, bd=15, width=300, height=250, relief=FLAT, bg=background)
	userFrame2.pack(padx=10, pady=30)


	backLbl = Button(root2, text='   Back   ', font=('Arial Bold', 10), bg=buttonbgcolor, fg='white', command=Backbtn, relief=FLAT)
	backLbl.place(x=10,y=5)


	#name
	nameLbl = Label(userFrame2, text='Username', font=('Arial Bold', 12), fg='black', bg=background)
	nameLbl.place(x=10,y=10)
	nameField = Entry(userFrame2, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
	nameField.focus()
	nameField.place(x=100,y=10)


	passwordLbl = Label(userFrame2, text='Password', font=('Arial Bold', 12), fg='black', bg=background)
	passwordLbl.place(x=10,y=50)
	passwordField = Entry(userFrame2, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7', show="*")
	passwordField.focus()
	passwordField.place(x=100,y=50)

	genLbl = Label(userFrame2, text='Gender', font=('Arial Bold', 12), fg='black', bg=background)
	genLbl.place(x=10,y=100)
	r = IntVar()
	s = ttk.Style()
	s.configure('Wild.TRadiobutton', background=background, foreground='black', font=('Arial Bold', 10), focuscolor=s.configure(".")["background"])
	genMale = ttk.Radiobutton(userFrame2, text='Male', value=1, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genMale.place(x=100,y=100)
	genFemale = ttk.Radiobutton(userFrame2, text='Female', value=2, variable=r, style='Wild.TRadiobutton', takefocus=False)
	genFemale.place(x=180,y=100)

	#agreement
	agr = IntVar()
	sc = ttk.Style()
	sc.configure('Wild.TCheckbutton', background=background, foreground='black', font=('Arial Bold',10), focuscolor=sc.configure(".")["background"])
	agree = Checkbutton(userFrame2, text='  I agree to use my files and\ncomputer setting', fg='black', bg="white", activebackground=background, activeforeground=textColor)
	agree = ttk.Checkbutton(userFrame2, text='  I agree to use my files and\n computer setting', style='Wild.TCheckbutton', takefocus=False, variable=agr)
	agree.place(x=28, y=150)

	#add face
	addBtn = Button(userFrame2, text='    submit    ', font=('Arial Bold', 12), bg=buttonbgcolor, fg='white', command=Nextstep, relief=FLAT)
	addBtn.place(x=90, y=200)

	#status of add face
	statusLbl = Label(root2, text='', font=('Arial 12'), fg='red', bg=background)
	statusLbl.place(x=180, y=20)


	###################### END OF REGISTER PAGE #####################

	######################  LOGIN PAGE #####################

	LoginFrame5 = Frame(root5, bd=10, bg=background)
	LoginFrame5.pack(fill=X)
	loginFrame = Frame(LoginFrame5, bd=15, width=300, height=250, relief=FLAT, bg=background)
	loginFrame.pack(padx=10, pady=30)

	backLbl1 = Button(root5, text='   Back   ', font=('Arial Bold', 10), bg=buttonbgcolor, fg='white', command=Backbtn, relief=FLAT)
	backLbl1.place(x=15,y=10)

	notreg = Label(root5, text='LOGIN', font=('Arial Bold', 18), fg="black", bg=background)
	notreg.place(x=200, y=10)

	#name
	nameLbl = Label(loginFrame, text='Username', font=('Arial Bold', 12), fg='black', bg=background)
	nameLbl.place(x=10,y=30)
	loginnameField = Entry(loginFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
	loginnameField.focus()
	loginnameField.place(x=100,y=30)


	passwordLbl = Label(loginFrame, text='Password', font=('Arial Bold', 12), fg='black', bg=background)
	passwordLbl.place(x=10,y=80)
	loginpasswordField = Entry(loginFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7', show="*")
	loginpasswordField.focus()
	loginpasswordField.place(x=100,y=80)


	lbutton=Button(root5, text='     LOGIN    ', bg=buttonbgcolor, fg='white',font=('Arial Bold', 12), bd=0, relief=FLAT,command=LoginCheck)
	lbutton.place(x=200,y=220)

	forgotpassbutton=Button(root5, text='     forgot password    ', bg=buttonbgcolor, fg='white',font=('Arial Bold', 12), bd=0, relief=FLAT,command=lambda:raise_frame(root6))
	forgotpassbutton.place(x=165,y=260)  

	notreg = Label(root5, text='Register if you not Register', font=('Arial 10'), fg="black", bg=background)
	notreg.place(x=190, y=180)

	#------------------------------ERROR MGS -----------------
	loginErrorLbl = Label(root5, text='', font=('Arial Bold',10), fg='red', bg=background)
	loginErrorLbl.place(x=130, y=40)

    ################## END OF LOGIN PAGE #####################

	######################  forgot LOGIN PAGE #####################

	forgotLoginFrame6 = Frame(root6, bd=10, bg=background)
	forgotLoginFrame6.pack(fill=X)
	forgotloginFrame = Frame(forgotLoginFrame6, bd=15, width=300, height=250, relief=FLAT, bg=background)
	forgotloginFrame.pack(padx=10, pady=30)

	backLbl1 = Button(root6, text='   Back   ', font=('Arial Bold', 10), bg=buttonbgcolor, fg='white', command=Backbtn, relief=FLAT)
	backLbl1.place(x=15,y=10)

	notreg = Label(root6, text='FORGOT PASSWORD', font=('Arial Bold', 12), fg="black", bg=background)
	notreg.place(x=160, y=28)

	#name
	nameLbl = Label(forgotloginFrame, text='Username', font=('Arial Bold', 12), fg='black', bg=background)
	nameLbl.place(x=10,y=50)
	loginnameField1 = Entry(forgotloginFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
	loginnameField1.focus()
	loginnameField1.place(x=100,y=50)

	showpasserror = Label(root6, text='', font=('Arial 12'), fg="red", bg=background)
	showpasserror.place(x=170, y=55)

	showpassword = Label(root6, text='', font=('Arial 12'), fg="red", bg=background)
	showpassword.place(x=230, y=150)


	showbutton=Button(root6, text='     show    ', bg=buttonbgcolor, fg='white',font=('Arial Bold', 12), bd=0, relief=FLAT,command=forgotpassword)
	showbutton.place(x=200,y=220) 



   ################### forgot OF LOGIN PAGE #####################

	#########################################
	######## SUCCESSFULL REGISTRATION #######
	#########################################

	userPIC = Label(root4, bg=background)
	userPIC.pack(pady=(40, 10))
	usernameLbl = Label(root4, text="", font=('Arial Bold',15), bg=background, fg='#85AD4F')
	usernameLbl.pack(pady=(0, 70))

	Label(root4, text="Your account has been successfully created!", font=('Arial Bold',15), bg=background, fg='#303E54', wraplength=300).pack(pady=10)
	Label(root4, text="Launch the APP again to get started the conversation with your Personal Assistant", font=('arial',13), bg=background, fg='#A3A5AB', wraplength=350).pack()

	Button(root4, text='     OK     ', bg=buttonbgcolor, fg='white',font=('Arial Bold', 18), bd=0, relief=FLAT, command=lambda:quit()).pack(pady=50)

	root.iconbitmap('extrafiles/images/aiicon.ico')
	raise_frame(root1)
	root.mainloop()
