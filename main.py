import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import threading



def talk(txt):
    engine.say(txt)
    engine.runAndWait()
# voice recognizer
listener = sr.Recognizer()
# initializing text to speech
engine= pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
talk("Hi. I am your virtual assistant. What can I do for you?")



def talk(txt):
    engine.say(txt)
    engine.runAndWait()

def main():
    try:
        with sr.Microphone() as source:
            print("listening..")
            voice = listener.listen(source)
            # voice to text
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                engine.runAndWait()
                command = command.replace('alexa', '').replace('hi', '').replace('hello', '').replace("hey",'').strip()
                print(command)
                run_va(command)
    except ValueError:
        print("No audio input detected.")    
    return command

def run_va(command):
    if "play" in command:
        song=command.replace('play','').replace("can",'')
        talk('playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("It is"+ time)
    elif "who is" in command or "what is" in command or "who's" in command or "what's" in command:
        question=command.replace("who is",'').replace("who's",'')\
            .replace("what is",'').replace("what's",'').strip()
        info=wikipedia.summary(question,2)
        print(info)
        talk(info)
    elif "joke" in command:
        if "chuck norris" in command:
            joke=pyjokes.get_joke(category='chuck')
        else:
            joke=pyjokes.get_joke(category='neutral')
        print(joke)
        talk(joke)


  
while True:
    user_command = main()
    if "stop" in user_command or "exit" in user_command or"bye" in user_command:
        break


