import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import openai

#  enter your open ai api key
openai.api_key="api_key"

# Initialize the OpenAI completion engine
completion=openai.Completion()

# Function to make Alexis speak the given text
def talk(txt):
    engine.say(txt)
    engine.runAndWait()

# Initialize the voice recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# greeting the user
talk("Hi. I am Alexis your virtual assistant. What can I do for you?")

# Function to play a song on YouTube based on the given query
def play_song(args):
    talk('playing ' + args)
    pywhatkit.playonyt(args)

# Function to get and speak the current time
def get_time(args):
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    talk("It is " + time)

# Function to get a Wikipedia summary for a given query
def get_wikipedia_summary(args):
    info = wikipedia.summary(args, 2)
    print(info)
    talk(info)

# Function to get a random joke and speak it
def get_joke(args):
    joke = pyjokes.get_joke()
    print(joke)
    talk(joke)

# Function to open a website based on the given query
def open_site(arg):
    sites=[("google", 'https://www.google.com/'),('wikipedia','https://www.wikipedia.org/'),('calculator',"https://www.desmos.com/scientific")]
    for site in sites:
        if site[0] in arg:
            talk ("opening"+ site[0])
            webbrowser.open(site[1])

# Function to use OpenAI API to generate a response for a given query
def ai(arg):
    try:
        prompt=arg
        reply=completion.create(prompt=prompt,engine="text-davinci-003",stop=None, max_tokens = 1024)
        answer=reply.choices[0].text.strip()
        print(answer)
        talk(answer)
    except Exception as e:
        print("Error with AI: ", e)
        talk("Sorry, there was an error processing your request.")

# Function to stop the program gracefully when the user commands "stop," "exit," or "bye"
def stop_program(args):
    global keep_listening
    keep_listening = False
    talk("Goodbye! Have a great day.")


def default_response():
    talk("Sorry, I have not been programmed for that task yet.")

#  Dictonary of tuples to map user commands to corresponding functions
commands = {
    "play": play_song,
    "time": get_time,
    "who is": get_wikipedia_summary,
    "who's": get_wikipedia_summary,
    "what is": get_wikipedia_summary,
    "what's": get_wikipedia_summary,
    "joke": get_joke,
    "open":open_site,
    "use ai":ai,
    "stop": stop_program,
    "exit": stop_program,
    "bye":stop_program
}

# Main function to handle user voice input and execute the corresponding commands
def main():
    global keep_listening
    keep_listening = True
    while keep_listening:
        try:
            with sr.Microphone() as source:
                print("listening..")
                voice = listener.listen(source, timeout=400)
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
                    talk("Goodbye! Have a great day.")
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