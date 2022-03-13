import pyttsx3 

def speak(text):
	engine = pyttsx3.init('sapi5')
	voices = engine.getProperty('voices')
	engine.setProperty('voices',voices[1].id)
	engine.setProperty('rate',180)
	engine.say(text=text)
	engine.runAndWait()