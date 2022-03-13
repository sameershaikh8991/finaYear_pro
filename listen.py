import speech_recognition as sr
from tkinter import *
from tkinter import ttk

def Listen():
	r = sr.Recognizer()
	# commandLbl['text'] = 'Listening...'

	with sr.Microphone() as source:
		print("Listneing...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing....")
		query = r.recognize_google(audio,language="en-in")
		print("user said:",query)
	except:
		return ""


	query = str(query)
	return query.lower()

# Listen()