# alexa

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value


listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hey how can i help you !!")
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'shona' in cmd:
                cmd = cmd.replace('shona', '')
                print(cmd)
            else:
                raise MyError("Use shona to search anything")
    except MyError as me:
        talk(me.value)
        exit()
    return cmd


def run_alexa():
    command1 = take_command()
    # print(command1)
    if 'play' in command1:
        song = command1.replace('shona', '')
        talk('playing song')
        pywhatkit.playonyt(song)
    elif 'time' in command1:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
    elif 'for loop' in command1:
        s = wikipedia.summary('For Loop', 2)
        talk(s)
    elif 'thank you' in command1:
        talk('My pleasure !!')
    elif 'by' in command1:
        talk('bye.take care')
        exit()
    elif 'have a nice day' in command1:
        talk("have a great day")
        exit()
    elif 'joke' in command1:
        talk(pyjokes.get_joke(language=''))
    else:
        talk("Please try again ")


run_alexa()


