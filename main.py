import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# voice recognizer
listener = sr.Recognizer()
# initializing text to speech
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(txt):
    engine.say(txt)
    engine.runAndWait()

def take_commands():
    try:
        with sr.Microphone() as source:
            print("I'm listening..")
            voice = listener.listen(source)
            # voice to text
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                engine.say("Hello, I am your virtual assistant.")
                engine.say("What can I do for you?")
                engine.runAndWait()
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_va():
    engine.runAndWait()
    command=take_commands()
    if "play" in command:
        song=command.replace('play','')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("It is"+ time)
run_va()
