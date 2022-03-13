import json
import random
import torch
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import webbrowser
import re
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from time import sleep
import os
from threading import Thread
# import pywhatkit
import smtplib
import string
#---------import from other file ----#

from brain import *
from NeuralNetwork import tokenize,bag_of_words
from systemapp import systemappfun,ringAlarm
from speak import speak
# from listen import Listen
from userHandler import UserData
# from setting import *
from menu import *
import appControl
from webapp import *
#-----------------------------------#

background, textColor = 'black', '#F6FAFB'
background,textColor = textColor, background

now = datetime.now()
currtime = now.strftime("%I:%M")
useremaildata =''
useremailpassdata=''
reciveremaildata =''
nowifiImg='extrafiles/images/nowifi.png'

global nowifi

userno =''
reciverno =''

# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device ='cpu'
with open('intent.json','r') as jsonData:
	intents = json.load(jsonData)


File = "traindata.pth"
data = torch.load(File)
input_size = data["input_size"]
hidden_size = data['hidden_size']
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
name ="mark"

def Listen():
	r = sr.Recognizer()
	commandLbl['text'] = 'Listening...'
	with sr.Microphone() as source:
		print("Listneing...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing....")
		commandLbl['text'] = 'Thinking...'
		query = r.recognize_google(audio,language="en-in")
		print("user said:",query)
	except:
		return 'None'


	query = str(query)
	return query.lower()


def voicefunction():
	# wishMe()
	# internetCheck()
	while True:
		query = Listen()
		if query == 'None':
			continue
		else: 
			mainfun(query.lower())


def addframe(text,bot=False):
	if bot:
		botchat = Label(chat_frame,text=text, bg="white", fg="black", justify=LEFT, wraplength=250, font=('Montserrat',12, 'bold'))
		botchat.pack(anchor='w',ipadx=20,ipady=5,pady=2,padx=20)
	else:
		userchat = Label(chat_frame, text=text, bg="#013c68", fg='white', justify=RIGHT, wraplength=250, font=('Montserrat',12, 'bold'))
		userchat.pack(anchor='e',ipadx=20,ipady=5,padx=20,pady=20)


def clearChatScreen():
	for wid in chat_frame.winfo_children():
		wid.destroy()



def usertextinput():
	pass

def SettingScreen():
	os.system('menu.py')


def raise_frame(frame):
	frame.tkraise()


def interneterror():
	root = Tk()
	root.title("Error")
	root.configure(bg='white')
	w_width, w_height = 400, 350
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.attributes('-topmost',True)
	# image1 = Image.open(nowifiImg)
	# image1 = image1.resize((130,130))
	# defaultImg1 = ImageTk.PhotoImage(image1)
	logo = Label(root, width=200, height=200, bg="white")
	logo.pack(padx=10, pady=5)
	# logo.image = nowifiImg

	msg = Label(root, text="no internet connection.\n make sure that your device is connected to internet", font=('Arial', 16), bg='white', wraplength=300)
	msg.place(x=60,y=200)
	exitbtn = Button(root, text='     OK     ', bg="#4361ee", fg='white',font=('Arial Bold', 14), bd=0, relief=FLAT, command=lambda:quit())
	exitbtn.place(x =150, y=310)
	
	root.iconbitmap('extrafiles/images/warning.ico')
	root.mainloop()


def internetCheck():
    url = "https://www.google.com"
    timeout = 2
    request = requests.get(url, timeout=timeout)


def sendEmaildata():
	global useremaildata, useremailpassdata,reciveremaildata
	useremaildata = userEmailEntry.get()
	useremailpassdata = userEmailpassEntry.get()
	reciveremaildata = reciverEmailEntry.get()
	# WAEMEntry.delete(0, END)
	userEmailEntry.delete(0, END)
	userEmailpassEntry.delete(0, END)
	reciverEmailEntry.delete(0, END)
	appControl.Win_Opt('close')


def send(e):
	sendEmaildata()


def sendmail(useremaildata,useremailpassdata,reciveremaildata):
	user = useremaildata
	password =useremailpassdata
	receiveremail = reciveremaildata
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	print("please follow this insrtuction from this link : https://tinyurl.com/5dudm8e3 \n to create email password ")
	server.login(user, password)
	commandLbl['text'] = 'Speaking...'
	speak("what should write in mail")
	content = Listen().lower()
	server.sendmail(user,receiveremail,content)
	speak("email send")
	server.close()

#-------------  	WHATSAPP --------------#
def sendwhatappdata():
	global userno,reciverno
	userno = userrnumberEntry.get()
	reciverno = recivernumberEntry.get()
	userrnumberEntry.delete(0, END)
	recivernumberEntry.delete(0, END)
	appControl.Win_Opt('close')

def sendwhatapp(e):
	sendwhatappdata()


def whatsapp(reciverno):
	phone_no = '+91' + str(reciverno)
	webbrowser.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
	import time
	from pynput.keyboard import Key, Controller
	time.sleep(10)
	k = Controller()
	k.press(Key.enter)

# ----------------------------------#
def textwinframe(text):
	if text == "email":
		global userEmailEntry,userEmailpassEntry,reciverEmailEntry,inputFrame
		inputFrame = Tk()
		inputFrame.title("Email")
		inputFrame.configure(bg='white')
		w_width, w_height = 600, 500
		s_width, s_height = inputFrame.winfo_screenwidth(), inputFrame.winfo_screenheight()
		x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
		inputFrame.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen

		Label(inputFrame, text="Enter Email Details", font=('Arial', 16), bg='white').pack(pady=(20, 10))
		userEmail = Label(inputFrame, text='Your email', font=('Arial Bold', 12), fg='black', bg="white")
		userEmail.place(x=10,y=80)
		userEmailEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
		userEmailEntry.focus()
		userEmailEntry.place(x=150,y=80)

		userEmailpass = Label(inputFrame, text='password', font=('Arial Bold', 12), fg='black', bg="white")
		userEmailpass.place(x=10,y=140)
		userEmailpassEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7', show="*")
		userEmailpassEntry.focus()
		userEmailpassEntry.place(x=150,y=140)


		reciverEmail = Label(inputFrame, text='Reciver email', font=('Arial Bold', 12), fg='black', bg="white")
		reciverEmail.place(x=10,y=200)
		reciverEmailEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
		reciverEmailEntry.focus()
		reciverEmailEntry.place(x=150,y=200)

		SendBtn = Button(inputFrame, text='Ok', font=('Arial', 12), relief=FLAT, bg='#14A769', fg='white', command=sendEmaildata)
		SendBtn.place(x=200,y=250)

		# noteL = Label(inputFrame, text='please follow this insrtuction from this link : https://tinyurl.com/5dudm8e3 \n to create email password', font=('Arial Bold', 10), fg='black', bg="white")
		# noteL.place(x=10,y=350)

		inputFrame.bind('<Return>', send)
		# inputFrame.destroy()
		inputFrame.iconbitmap('extrafiles/images/email.ico')
		inputFrame.mainloop()
	else:
		inputFrame = Tk()
		inputFrame.title("whatsapp")
		inputFrame.configure(bg='white')
		w_width, w_height = 400, 350
		s_width, s_height = inputFrame.winfo_screenwidth(), inputFrame.winfo_screenheight()
		x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
		inputFrame.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen

		Label(inputFrame, text="Enter Email Details", font=('Arial', 16), bg='white').pack(pady=(20, 10))
		usernumber = Label(inputFrame, text='Your number', font=('Arial Bold', 12), fg='black', bg="white")
		userrnumber.place(x=10,y=80)
		userrnumberEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
		userrnumberEntry.focus()
		userrnumberEntry.place(x=150,y=80)


		recivernumber = Label(inputFrame, text='Reciver number', font=('Arial Bold', 12), fg='black', bg="white")
		recivernumber.place(x=10,y=200)
		recivernumberEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=25, relief=FLAT, bg='#D4D5D7')
		recivernumberEntry.focus()
		recivernumberEntry.place(x=150,y=200)

		SendBtn = Button(inputFrame, text='Ok', font=('Arial', 12), relief=FLAT, bg='#14A769', fg='white', command="sendWAEM")
		SendBtn.place(x=200,y=250)
		inputFrame.bind('<Return>', send)

		inputFrame.iconbitmap('extrafiles/images/email.ico')
		inputFrame.mainloop()



try:
	user = UserData()
	user.extractData()
	ownerName = user.getName().split()[0]
	ownerDesignation = "Sir"
	# if user.getGender()=="Female": ownerDesignation = "Ma'am"
except Exception as e:
	print("You're not Registered Yet")
	os.system('python start.py')



def alarmcheck():
	time_to_set = open('time.txt','r')
	time_now = time_to_set.read()
	time_now = time_now.replace("and",":")
	time_now = time_now.replace(" ","")

	Alarm_time = str(time_now)
	print(Alarm_time)

	current_time = datetime.now().strftime("%H:%M")
	if current_time == Alarm_time:
		ringAlarm()
	else:
		exit()

def latestNews(news=5):
	URL = 'https://indianexpress.com/latest-news/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	headlines = []

	divs = soup.find_all('div', {'class':'title'})

	count=0
	for div in divs:
		count += 1
		if count>news:
			break
		a_tag = div.find('a')
		headlines.append(a_tag.text)

	return headlines

def mainfun(text):
	# print("enter in loop")
	addframe(text,False)
	query = text
	result = str(query)
	
	if query =="exit":
		exit()

	query = tokenize(query)
	p1 = bag_of_words(query, all_words)
	p1 = p1.reshape(1,p1.shape[0])
	p1 = torch.from_numpy(p1).to(device)


	output = model(p1)

	_ ,predict = torch.max(output,dim=1)

	tag = tags[predict.item()]

	probs = torch.softmax(output,dim=1)
	prob = probs[0][predict.item()]

	if prob.item() > 0.75:
		for intent in intents['intents']:
			if tag == intent['tag']:
				respon = random.choice(intent['respones'])
				# print(respon)
				if "time" in respon:
					time = datetime.now().strftime("%H:%M")
					addframe(time,True)
					speak(time)
					clearChatScreen()
				elif "date" in respon:
					date = datatime.date.today()
					addframe(date,True)
					commandLbl['text'] = 'Speaking...'
					speak(date)
					clearChatScreen()

				elif "googlesearch" in respon:
					print("googlesearch")
					import wikipedia as glgscrap
					query = result.replace("search ","")
					query = result.replace("search on","")
					query = result.replace("search on google","")
					query = result.replace("google","")
					query = result.replace("search on","")
					commandLbl['text'] = 'Speaking...'
					speak("i find someting on web")
					try:
						import pywhatkit
						pywhatkit.search(query)
						res = glgscrap.summary(query,3)
						commandLbl['text'] = 'Speaking...'
						speak(res)
						print(res)
					except:
						speak("not speakable")

				elif "wiki" in respon:
					# inputExc(tag, result)
					pass
				elif 'google' in respon:
					webbrowser.open(respon)
					clearChatScreen()

				elif 'youtube' in respon:
					webbrowser.open(respon)
					clearChatScreen()

				elif 'map' in respon:
					query = result.replace("show map","")
					query = result.replace("show location","")
					query = result.replace("map","")
					webbrowser.open('https://www.google.com/maps/place/'+query)

				elif "email" in respon:
					commandLbl['text'] = 'Speaking...'
					speak('Whom do you want to send the email?')
					addframe('Whom do you want to send the email?',True)
					textwinframe(text='email')
					Thread(target=sendmail,args=(useremaildata,useremailpassdata,reciveremaildata)).start()
					clearChatScreen()
					return
				elif "whatsapp" in respon:
					commandLbl['text'] = 'Speaking...'
					speak("whom do you want to send")
					textwinframe(whatsapp)
					Thread(target=sendwhatapp,args=(userno,reciverno)).start()
				elif 'createfolder' in respon:
					systemappfun(respon)
					clearChatScreen()

				elif 'password' in respon:
					systemappfun(respon)
					clearChatScreen()

				elif 'screenshot' in respon:
					systemappfun(respon)
					clearChatScreen()

				elif 'createtodo' in respon:
					tag = "createtodo"
					systemappfun(tag)
					clearChatScreen()

				elif 'showtodo' in respon:
					tag = 'showtodo'
					systemappfun(tag)
					clearChatScreen()

				elif 'showremind' in respon:
					tag ='showremind'
					systemappfun(tag)
				elif 'remind' in respon:
					tag ='remind'
					systemappfun(tag)

				elif 'mword' in respon:
					tag ='mword'
					systemappfun(tag)

				elif 'mppt' in respon:
					tag ='mppt'
					systemappfun(tag)

				elif 'mexcel' in respon:
					tag ='mexcel'
					systemappfun(tag)

				elif 'alarm' in respon:
					tag = 'alarm'
					systemappfun(tag)

				elif 'downloadutubevid' in respon:
					print("enter in loop....")
					tag = "downloadutubevid"
					webappfun(tag)
				elif 'news' in respon:
					speak("getting news")
					news = latestNews()
					for i in news:
						addframe(i,True)
						speak(i)
						clearChatScreen()
				else:
					if respon != "":
						speak(respon)
						addframe(respon,True)
						clearChatScreen()




def progressbar():
	s = ttk.Style()
	s.theme_use('clam')
	s.configure("white.Horizontal.TProgressbar", foreground='white', background='white')
	progress_bar = ttk.Progressbar(splash_root,style="white.Horizontal.TProgressbar", orient="horizontal",mode="determinate", length=303)
	progress_bar.pack()
	splash_root.update()
	progress_bar['value'] = 0
	splash_root.update()
 
	while progress_bar['value'] < 100:
		progress_bar['value'] += 5
		# splash_percentage_label['text'] = str(progress_bar['value']) + ' %'
		splash_root.update()
		sleep(0.1)

def destroySplash():
	splash_root.destroy()


if __name__=='__main__':
	splash_root = Tk()
	splash_root.configure(bg='#013c68')
	splash_root.overrideredirect(True)
	splash_label = Label(splash_root, text="Starting Application", font=('montserrat',15),bg='#013c68',fg='white')
	splash_label.pack(pady=40)
	# splash_percentage_label = Label(splash_root, text="0 %", font=('montserrat',15),bg='#3895d3',fg='white')
	# splash_percentage_label.pack(pady=(0,10))

	w_width, w_height = 400, 200
	s_width, s_height = splash_root.winfo_screenwidth(), splash_root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	splash_root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))

	progressbar()
	splash_root.after(10, destroySplash)
	splash_root.mainloop()

	root = Tk()
	s = ttk.Style()
	s.theme_use('xpnative')
	root.title('MARK')
	w_width, w_height = 450, 600
	s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
	x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
	root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen
	root.configure(bg=background)
	root.resizable(0, 0)
	root.pack_propagate()

	root1 = Frame(root, bg=background)
	root2 = Frame(root, bg="green")
	root3 = Frame(root, bg=background)

	for allf in (root1, root2, root3):
		allf.grid(row=0, column=0, sticky='news')



	chat_frame = Frame(root1, width=450,height=520,bg="#edede9")
	chat_frame.pack(padx=0)
	chat_frame.pack_propagate(0)

	bottomFrame1 = Frame(root1, bg='white', height=100)
	bottomFrame1.pack(fill=X, side=BOTTOM)
	VoiceModeFrame = Frame(bottomFrame1, bg='#e9ecef')
	VoiceModeFrame.pack(fill=BOTH)

	image = Image.open("extrafiles/images/inputbox.png")

	resize_image = image.resize((300, 70))

	cblLightImg = ImageTk.PhotoImage(resize_image)

	cbl = Label(VoiceModeFrame, image=cblLightImg, bg='#dfdfdf',width=300)
	cbl.pack(pady=2)


	commandLbl = Label(VoiceModeFrame, text='Offline', fg='white',bg="#013c68", font=('montserrat', 16))
	commandLbl.place(x=140,y=20)

	sphDark = PhotoImage(file = "extrafiles/images/menu.png")
	sphDark = sphDark.subsample(1,1)
	settingBtn = Button(VoiceModeFrame,image=sphDark, bg='white', fg='white',font=('Arial Bold',30), activebackground="#0077b6",bd=0, relief=FLAT,command=SettingScreen)
	settingBtn.place(x=380,y=8)

	wifierrFrame = Frame(root2, bd=10, bg=background)
	wifierrFrame.pack(fill=X)
	wifierrpageFrame = Frame(wifierrFrame, bd=15, width=310, height=500, relief=FLAT, bg=background)
	wifierrpageFrame.pack(padx=10, pady=30)

	# logo = Label(root2, width=200, height=200, image="defaultImg1",bg="white")
	# logo.pack(padx=10, pady=5)

	msg = Label(wifierrpageFrame, text="no internet connection.\n make sure that your device is connected to internet", font=('Arial', 16), bg='white', wraplength=300)
	msg.place(x=60,y=200)
	exitbtn = Button(wifierrpageFrame, text='     OK     ', bg="#4361ee", fg='white',font=('Arial Bold', 14), bd=0, relief=FLAT, command=lambda:quit())
	exitbtn.place(x =150, y=310)

	try:
		url = "https://www.google.com"
		timeout = 2
		request = requests.get(url, timeout=timeout)
		print("work fine")
	except (requests.ConnectionError, requests.Timeout) as exception:
		interneterror()
		# speak("sir please check your internet connection")
		# raise_frame(root2)


	try:
		Thread(target=voicefunction).start()
		# Thread(target=alarmcheck).start()
		# pass
	except:
		print("someting happend wrong!")

	root.iconbitmap('extrafiles/images/aiicon.ico')
	raise_frame(root1)
	root.mainloop()