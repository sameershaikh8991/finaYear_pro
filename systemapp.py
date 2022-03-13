from datetime import datetime
import os
import pyautogui
import random
from speak import speak
import string
import subprocess
# from listen import Listen

def createFolder():
    speak("name for the folder")
    from main import Listen
    folderName = Listen().lower()
    path_dir = 'C:/Users/'+os.getlogin()+'/Desktop/'
    path = os.path.join(path_dir, folderName)
    mode =0o666
    os.mkdir(path, mode)
    speak("Sir folder created")


def passwordgen():
    length = 8                  
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    print("password:",password)


def takescreenshot():
    speak("taking screenshot")
    myScreenshot = pyautogui.screenshot()
    myScreenshotName = random.randint(1, 100)
    myScreenshot.save(r'C:/Users/'+os.getlogin()+'/Pictures/Screenshots/{}.png'.format(myScreenshotName))
    speak("screenshot save in screenshot folder")



file = "TODOList.txt"

def createTodofile():
    f = open(file,"w")
    present = datetime.now()
    dt_format = present.strftime("Date: " + "%d/%m/%Y"+ "\n")
    f.write(dt_format)
    f.close()

def toDoList(text):
    if os.path.isfile(file) == False:
        createTodofile()
    f = open(file,"r")
    x = f.read(8)
    f.close()
    y = x[6:]
    yesterday = int(y)
    present = datetime.now()
    today = int(present.strftime("%d"))
    if (today-yesterday) >= 1:
        createTodofile()
    f = open(file,"a")
    dt_format = present.strftime("%H:%M")
    print(dt_format)
    f.write(f"[{dt_format}] : {text}\n")
    f.close()

def showtoDoList():
    if os.path.isfile(file)==False:
        print("todo list is empty")
        return 
    else:
        f = open(file, 'r')
        
        items = []
        for line in f.readlines():
            items.append(line.strip())

        speakList = [f"You have {len(items)-1} items in your list:\n"]
        for i in items[1:]:
            speakList.append(i.capitalize())
        return speakList



def remind():
    speak("what should i remember sir")
    rememberMessage = Listen().lower()
    remember = open('rememberdata.txt','w')
    remember.write(rememberMessage)
    remember.close()
    speak("remember saved")

def showremind():
    rememberMessage = open('rememberdata.txt','r')
    msg = rememberMessage.read()
    l = len(msg)
    if l!=0:
        speak(msg)
    else:
        speak("no reminder")


def createFile(text):
    if (text =='powerpoint'):
        file_name == "sample_file.ppt"
        appLocation = "C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Microsoft\\WindowsApps"

    elif (text =='excel'):
        file_name = "sample_file.xsl"
        appLocation = "C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Microsoft\\WindowsApps"

    elif (text=='word'):
        file_name = "sample_file.docx"
        appLocation =  "C:\\Users\\"+os.getlogin()+"\\AppData\\Local\\Microsoft\\WindowsApps"

    elif (text =='text'): file_name = "sample_file.txt"
    elif "python" in text: file_name = "sample_file.py"
    elif "css" in text: file_name = "sample_file.css"
    elif "javascript" in text: file_name = "sample_file.js"
    elif "html" in text: file_name = "sample_file.html"
    elif "c plus plus" in text or "c + +" in text: file_name = "sample_file.cpp"
    elif "java" in text: file_name = "sample_file.java"
    elif "json" in text: file_name = "sample_file.json"
    else: return "Unable to create this type of file"

    file = open(path + file_name, 'w')
    file.close()
    subprocess.Popen([appLocation, path + file_name])
    return "File is created.\nNow you can edit this file"



filelocation = 'C:/Users/'+os.getlogin()+'/Desktop/'
def mword():
    file_name ='sample.docx'
    appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.EXE"
    subprocess.Popen([appLocation,filelocation + file_name])
    speak("File is create \n nNow you can edit this file")
    return "File is create \n nNow you can edit this file"


def mwppt():
    file_name = "sample_file.ppt"
    appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"
    subprocess.Popen([appLocation,filelocation + file_name])
    speak("File is create \n nNow you can edit this file")
    return "File is create \n nNow you can edit this file"


def mexcel():
    file_name = "sample_file.xsl"
    appLocation = "C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.EXE"
    subprocess.Popen([appLocation,filelocation + file_name])
    speak("File is create \n nNow you can edit this file")
    return "File is create \n nNow you can edit this file"





def alarm(time):
    time_to_set = str(time)
    time_now = time_to_set.replace("jarvis","")
    time_now = time_to_set.replace("set alram for","")
    time_now = time_to_set.replace("time","")
    time_now = time_to_set.replace("alram","")
    time_now = time_to_set.replace("for","")
    time_now = time_to_set.replace("and",":")

    Alarm_time = str(time_now)
    speak("alarm set")


def ringAlarm():
    print("wake up")

def systemappfun(tag):
    if "createfolder" in tag:
        createFolder()

    elif "password" in tag:
        passwordgen()

    elif "screenshot" in tag:
        takescreenshot()

    elif 'showtodo' in tag:
        items = showtoDoList()
        if len(items)==1:
            speak(items[0])
            return
        speak(items[0])

    elif 'createtodo' in tag:
        speak("What do you want to add?")
        from main import Listen
        item = Listen().lower()
        toDoList(item)
        speak("Alright, I added to your list")

    elif 'remind' in tag:
        remind()

    elif 'showremind' in tag:
        showremind()

    elif 'mexcel' in tag:
        mword()


    elif 'mppt' in tag:
        mwppt()

    elif 'mword' in tag:
        mword()
        
    elif 'alarm' in tag:
        from listen import Listen
        speak("sir till me time for alarm")
        query = Listen().lower()
        print(query)
        timedata = open('time.txt','a')
        timedata.write(query)
        timedata.close()

        extreact_timedata = open('time.txt','rt')
        time = extreact_timedata.read()
        Time = str(time)

        # delete_time = open('time.txt','r+')
        # delete_time.truncate(0)
        # delete_time.close()
        alarm(query)
    else:
        print("no...")