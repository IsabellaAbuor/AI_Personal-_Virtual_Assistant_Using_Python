import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
from time import strftime
from tkinter import *

print('Say something...')
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def CommandsList():
    '''show the command to which voice assistant is registered with'''
    os.startfile('')

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            talk("""
            Hello. Good Morning
            I am Alexa and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you. 
            """)
        elif 12 <= day_time < 18:
            talk("""
            Hello. Good Afternoon
            I am Alexa and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you. 
            """)
        else:
            talk("""
            Hello. Good evening
            I am Alexa and I am your personal voice assistant, Please give a command or say "help me" and I will tell you what all I can do for you. 
            """)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry,I have a headache')
    elif 'are you single' in command:
        talk('Im married to the idea of helping people')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'help me' in command:
        talk("""
            You can use these commands and I'll help you out:
            1. To wake up the Assistant we use the word 'Alexa'
            2. Play 'name of the song/ Artist':Plays a song on youtube  
            3. time : Current system time
            4. Tell a joke/another joke : Says a random dad joke.
            5. who is : Tells you a summary of who the person is on wikipedia 
            6. Open: Launches an system application
            7. Ask it anything 
            """)
    elif 'open' in command:
        talk('Opening Settings')
        os.startfile('C:\Windows\System32\control.exe')
    elif 'launch chrome' in command:
        talk("Opening chrome")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs')
    elif 'notepad' in command:
        talk('Opening notepad')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories')
    elif 'paint' in command:
        talk("Opening Microsoft paint....")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories')
    else:
        talk('Come again?')


while True:
    run_alexa()

    # tkinter code
    root = Tk()

    # Create the menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    #Create Submenu

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=subMenu)
    subMenu.add_command(label='Commands List', command=CommandsList)

    subMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Settings',menu=subMenu)

    root.geometry("{}x{}+{}+{}".format(745, 360, int(root.winfo_screenwidth() / 2 - 745 / 2),
                                       int(root.winfo_screenheight() / 2 - 360 / 2)))
    root.resizable(0,0)
    root.title("Alexa")
    root.iconbitmap(r'icon.ico')
    root.configure(bg='#000080')

    Photo = PhotoImage(file='mic.png')

    btn = Button(root, image=Photo, borderwidth=0, activebackground='#2c4557', bg='#000080', command=run_alexa)
    btn.place(x=330, y=280)


    root.mainloop()
