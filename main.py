import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


def talk(txt):
    engine.say(txt)
    engine.runAndWait()

# voice recognizer
listener = sr.Recognizer()
# initializing text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
talk("Hi. I am Alexis your virtual assistant. What can I do for you?")

def play_song(args):
    talk('playing ' + args)
    pywhatkit.playonyt(args)

def get_time(args):
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    talk("It is " + time)

def get_wikipedia_summary(args):
    info = wikipedia.summary(args, 2)
    print(info)
    talk(info)

def get_joke(args):
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)

def open_site(arg):
    sites=[("google", 'https://www.google.com/'),('wikipedia','https://www.wikipedia.org/'),('calculator',"https://www.desmos.com/scientific")]
    for site in sites:
        if site[0] in arg:
            talk ("opening"+ site[0])
            webbrowser.open(site[1])

def default_response():
    talk("Sorry, I have not been programmed for that task yet.")

commands = {
    "play": play_song,
    "time": get_time,
    "who is": get_wikipedia_summary,
    "who's": get_wikipedia_summary,
    "what is": get_wikipedia_summary,
    "what's": get_wikipedia_summary,
    "joke": get_joke,
    "open":open_site,
}

def main():
    keep_listening = True
    while keep_listening:
        try:
            with sr.Microphone() as source:
                print("listening..")
                voice = listener.listen(source, timeout=200)
                # Voice to text
                command = listener.recognize_google(voice)
                command = command.lower()
                if "alexis" in command:
                    engine.runAndWait()
                    command = command.replace('alexis', '').replace('hi', '').replace('hello', '').replace("hey",'').strip()
                    print(command)
                    run_va(command)
                if "stop" in command or "exit" in command or "bye" in command:
                    keep_listening = False
        except ValueError:
            print("No audio input detected.")
            continue
        except:
            pass


def run_va(command):
    for keyword, func in commands.items():
        if keyword in command:
            argument = command.replace(keyword, '').strip()
            func(argument)
            return
    default_response()

main()