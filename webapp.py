import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from main import Listen
from speak import speak
import smtplib
import pytube  
from pytube import YouTube
import appControl
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

video_url =""


def getDirection():
	speak("start point")
	startpoint = take_command().lower()
	speak("destination")
	destinationPoint = take_command().lower()
	geolocator = Nominatim(user_agent='assistant')
	if 'current' in startpoint:
		res = requests.get("https://ipinfo.io/")
		data = res.json()
		startinglocation = geolocator.reverse(data['loc'])
	else:
		startinglocation = geolocator.geocode(startpoint)

	destinationloc = geolocator.geocode(destinationPoint)
	webbrowser.open('https://www.google.co.in/maps/dir/'+startpoint+'/'+destinationPoint)




def sendDtofun():
	global video_url
	video_url = youtubelinkEntry.get()
	youtubelinkEntry.delete(0, END)
	appControl.Win_Opt('close')
	downloadutubevid()

def downloadutubevid():
	global video_url
	# speak("Enter video link")
	youtube = pytube.YouTube(str(video_url))
	video = youtube.streams.first()
	video.download('C:/Users/'+os.getlogin()+'/Downloads')
	speak("Video downloaded")
	print("video download.......")

def send(e):
	sendDtofun()
	

def textwinframe(text):
	if text == "youtube":
		global youtubelinkEntry,inputFrame
		inputFrame = Tk()
		inputFrame.title("Email")
		inputFrame.configure(bg='white')
		w_width, w_height = 400, 200
		s_width, s_height = inputFrame.winfo_screenwidth(), inputFrame.winfo_screenheight()
		x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
		inputFrame.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30)) #center location of the screen

		Label(inputFrame, text="Download youtube video", font=('Arial', 16), bg='white').pack(pady=(20, 10))
		youtubelink = Label(inputFrame, text='Enter Youtube \nLink:', font=('Arial Bold', 12), fg='black', bg="white",wraplength=200)
		youtubelink.place(x=10,y=80)
		youtubelinkEntry = Entry(inputFrame, bd=5, font=('Arial Bold', 10), width=30, relief=FLAT, bg='#D4D5D7')
		youtubelinkEntry.focus()
		youtubelinkEntry.place(x=140,y=80)
		
		SendBtn = Button(inputFrame, text='Download', font=('Arial', 12), relief=FLAT, bg='#14A769', fg='white', command=sendDtofun)
		SendBtn.place(x=170,y=130)
		inputFrame.bind('<Return>', send)
		# inputFrame.destroy()
		inputFrame.iconbitmap('extrafiles/images/youtube.ico')
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




def webappfun(tag):
	if 'news' in tag:
		latestNews()
	elif 'direction' in tag:
		getDirection()
	elif 'downloadutubevid' in tag:
		print("enter in webapp loop...")
		textwinframe(text='youtube')
	else:
		pass