import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk('Good Morning!')
    elif hour >= 12 and hour < 18:
        talk('Good Afternoon')
    else:
        talk('Good Evening')

    talk('I am voxinnovate, How may I help you?')


def run_alexa():
    wishme()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open google' in command:
        wb.open('https://www.google.co.in/?client=safari&channel=mac_bm')
    elif 'open safari' in command:
        wb.open('https://www.apple.com/in/safari/')
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk('According to Wikipedia')
        print(info)
        talk(info)
    elif 'what is' in command:
        car = command.replace('what is', '')
        info = wikipedia.summary(car, 1)
        talk('According to Wikipedia')
        print(info)
        talk(info)
    elif 'be thankful' in command:
        talk('Thank you for giving us this opportunity to prove our talent')

    else:
        talk('Please say the command again.')


while True:
    run_alexa()